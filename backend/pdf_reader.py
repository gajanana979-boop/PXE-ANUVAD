import fitz


def extract_pdf_blocks(pdf_path):
    """
    Extract text blocks with layout information while preserving
    font, size, color, direction and coordinates.
    """

    document = fitz.open(pdf_path)

    extracted_blocks = []

    for page_number in range(len(document)):

        page = document[page_number]

        page_dict = page.get_text("dict")

        for block in page_dict["blocks"]:

            # Ignore images
            if block["type"] != 0:
                continue

            for line in block["lines"]:

                line_text = ""

                spans = []

                for span in line["spans"]:

                    text = span["text"]

                    if not text.strip():
                        continue

                    line_text += text

                    spans.append({

                        "text": text,

                        "bbox": span["bbox"],

                        "font": span["font"],

                        "size": span["size"],

                        "color": span["color"],

                        "flags": span["flags"]

                    })

                if not line_text.strip():
                    continue

                extracted_blocks.append({

                    "page": page_number,

                    "bbox": line["bbox"],

                    "text": line_text,

                    # Writing direction
                    "dir": line.get("dir", (1.0, 0.0)),

                    # Writing mode (horizontal / vertical)
                    "wmode": line.get("wmode", 0),

                    "spans": spans

                })

    document.close()

    return extracted_blocks


if __name__ == "__main__":

    pdf_path = input("Enter PDF Path: ")

    blocks = extract_pdf_blocks(pdf_path)

    print("\nTotal Lines :", len(blocks))

    print("\nFirst 3 Lines\n")

    for block in blocks[:3]:

        print("=" * 70)

        print("Page :", block["page"] + 1)

        print("Text :", block["text"])

        print("BBox :", block["bbox"])

        print("Direction :", block["dir"])

        print("Writing Mode :", block["wmode"])

        print()

        print("Span Information:")

        for span in block["spans"]:
            print(span)

        print()