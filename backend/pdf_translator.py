from pdf_reader import extract_text_from_pdf
from language_detector import detect_language
from translator import translate


def translate_pdf(pdf_path, target_language):

    pages = extract_text_from_pdf(pdf_path)

    translated_document = ""

    for page in pages:

        translated_document += f"\n========== PAGE {page['page']} ==========\n\n"

        for paragraph in page["paragraphs"]:

            # Split paragraph into lines
            lines = paragraph.split("\n")

            for line in lines:

                line = line.strip()

                if not line:
                    translated_document += "\n"
                    continue

                source_language = detect_language(line)

                translated_line = translate(
                    text=line,
                    source_language=source_language,
                    target_language=target_language
                )

                translated_document += translated_line + "\n"

            translated_document += "\n"

    return translated_document


if __name__ == "__main__":

    pdf_path = input("Enter PDF Path: ")

    target_language = input("Target Language: ")

    output = translate_pdf(
        pdf_path,
        target_language
    )

    print(output)