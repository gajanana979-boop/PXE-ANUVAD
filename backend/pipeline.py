from file_handler import validate_file
from pdf_reader import extract_pdf_blocks
from ocr import OCRReader
from text_preprocessor import clean_text
from language_detector import detect_language
from translator import translate


class TranslationPipeline:

    def __init__(self):

        self.ocr = OCRReader()


    def process_document(self, file_path, target_language):

        file_type = validate_file(file_path)

        # ---------- PDF ----------
        if file_type == "PDF":

            blocks = extract_pdf_blocks(file_path)

            # If no text found, it is probably a scanned PDF
            if len(blocks) == 0:

                print("\nScanned PDF detected.")
                print("Switching to OCR...\n")

                blocks = self.ocr.extract_pdf(file_path)

        # ---------- IMAGE ----------
        else:

            blocks = self.ocr.extract_text(file_path)


        # ---------- CLEAN ALL TEXT BLOCKS ----------

        cleaned_blocks = []

        for block in blocks:

            text = clean_text(block["text"])

            if not text:
                continue

            cleaned_blocks.append({

                "block": block,

                "text": text

            })


        # No readable text found
        if not cleaned_blocks:

            return []


        # ---------- DETECT DOCUMENT LANGUAGE ONCE ----------

        complete_text = " ".join(

            item["text"]

            for item in cleaned_blocks

        )

        document_source_language = detect_language(
            complete_text
        )

        print(
            "\nDetected Document Language:",
            document_source_language
        )


        # ---------- TRANSLATE ALL BLOCKS ----------

        translated_blocks = []

        for item in cleaned_blocks:

            block = item["block"]

            text = item["text"]

            if document_source_language == "Unknown":

                translated_text = text

            else:

                translated_text = translate(

                    text,

                    document_source_language,

                    target_language

                )


            translated_blocks.append({

                "page": block.get("page", 0),

                "bbox": block["bbox"],

                "original_text": text,

                "translated_text": translated_text,

                "spans": block.get("spans", [])

            })


        return translated_blocks


if __name__ == "__main__":

    pipeline = TranslationPipeline()

    file_path = input(
        "Enter File Path : "
    ).strip()

    target_language = input(
        "Target Language : "
    ).strip()

    translated_blocks = pipeline.process_document(

        file_path,

        target_language

    )

    print(
        "\nTotal Translated Blocks :",
        len(translated_blocks)
    )

    if translated_blocks:

        print("\nFirst Block\n")

        print(translated_blocks[0])
