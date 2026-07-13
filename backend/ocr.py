import fitz
import easyocr
import numpy as np


class OCRReader:

    def __init__(self):

        print("Loading EasyOCR model...")

        self.reader = easyocr.Reader(
            ['hi','en'],
            gpu=False
        )

        print("EasyOCR Ready!\n")

    def extract_text(self, image):

        results = self.reader.readtext(image)

        extracted_data = []

        for result in results:

            bbox, text, confidence = result

            x0 = min(point[0] for point in bbox)
            y0 = min(point[1] for point in bbox)
            x1 = max(point[0] for point in bbox)
            y1 = max(point[1] for point in bbox)

            extracted_data.append({

                "page": 0,

                "bbox": (x0, y0, x1, y1),

                "text": text,

                "confidence": confidence,

                "spans": [{
                    "size": 12
                }]

            })

        return extracted_data

    def extract_pdf(self, pdf_path):

        document = fitz.open(pdf_path)

        all_blocks = []

        zoom = 2

        for page_number in range(len(document)):

            page = document[page_number]

            page_width = page.rect.width
            page_height = page.rect.height

            pix = page.get_pixmap(
                matrix=fitz.Matrix(zoom, zoom)
            )

            image = np.frombuffer(
                pix.samples,
                dtype=np.uint8
            )

            image = image.reshape(
                pix.height,
                pix.width,
                pix.n
            )

            results = self.reader.readtext(image)

            scale_x = page_width / pix.width
            scale_y = page_height / pix.height

            for result in results:

                bbox, text, confidence = result

                x0 = min(point[0] for point in bbox) * scale_x
                y0 = min(point[1] for point in bbox) * scale_y
                x1 = max(point[0] for point in bbox) * scale_x
                y1 = max(point[1] for point in bbox) * scale_y

                all_blocks.append({

                    "page": page_number,

                    "bbox": (
                        x0,
                        y0,
                        x1,
                        y1
                    ),

                    "text": text,

                    "confidence": confidence,

                    "spans": [{
                        "size": 12
                    }]

                })

        document.close()

        return all_blocks


if __name__ == "__main__":

    path = input("Enter Image/PDF Path : ").strip()

    ocr = OCRReader()

    if path.lower().endswith(".pdf"):

        blocks = ocr.extract_pdf(path)

    else:

        blocks = ocr.extract_text(path)

    print("\nDetected :", len(blocks), "blocks")

    print()

    for block in blocks[:10]:

        print("=" * 60)
        print("Page :", block["page"] + 1)
        print("Text :", block["text"])
        print("BBox :", block["bbox"])
        print("Confidence :", round(block["confidence"], 3))
