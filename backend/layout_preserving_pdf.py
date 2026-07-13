import os
import fitz

from pipeline import TranslationPipeline
from layout_cleaner import add_redaction, apply_redactions
from layout_writer import write_text
from file_handler import validate_file


def image_to_pdf(image_path):
    """
    Convert an image into a temporary PDF while preserving
    the original image dimensions.
    """

    image_document = fitz.open(image_path)

    pdf_bytes = image_document.convert_to_pdf()

    image_document.close()

    pdf_document = fitz.open(
        "pdf",
        pdf_bytes
    )

    return pdf_document


def translate_pdf(input_file, output_pdf, target_language):

    # Detect whether input is PDF or image
    file_type = validate_file(input_file)

    # Run OCR / text extraction / translation
    pipeline = TranslationPipeline()

    translated_blocks = pipeline.process_document(
        input_file,
        target_language
    )

    # Open PDF normally
    if file_type == "PDF":

        document = fitz.open(input_file)

    # Convert image to an in-memory PDF
    else:

        document = image_to_pdf(input_file)

    # Process page by page
    for page_number in range(len(document)):

        page = document[page_number]

        page_blocks = [
            block
            for block in translated_blocks
            if block["page"] == page_number
        ]

        # STEP 1: Add all redactions
        for block in page_blocks:

            add_redaction(
                page,
                block["bbox"]
            )

        # STEP 2: Apply all redactions once
        if page_blocks:

            apply_redactions(page)

        # STEP 3: Insert translated text
        for block in page_blocks:

            write_text(
                page,
                block,
                block["translated_text"]
            )

    document.save(
        output_pdf,
        garbage=4,
        deflate=True
    )

    document.close()


if __name__ == "__main__":

    input_file = input("Input File: ").strip()

    output_pdf = input("Output PDF: ").strip()

    target_language = input("Target Language: ").strip()

    translate_pdf(
        input_file,
        output_pdf,
        target_language
    )

    print("\nTranslated PDF Saved Successfully!")
