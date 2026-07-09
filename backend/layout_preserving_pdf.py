import fitz

from pipeline import TranslationPipeline
from layout_cleaner import add_redaction, apply_redactions
from layout_writer import write_text


def translate_pdf(input_pdf, output_pdf, target_language):

    pipeline = TranslationPipeline()

    translated_blocks = pipeline.process_document(
        input_pdf,
        target_language
    )

    document = fitz.open(input_pdf)

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

        # STEP 2: Apply redactions once
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

    input_pdf = input("Input PDF: ")

    output_pdf = input("Output PDF: ")

    target_language = input("Target Language: ")

    translate_pdf(
        input_pdf,
        output_pdf,
        target_language
    )

    print("\nTranslated PDF Saved Successfully!")