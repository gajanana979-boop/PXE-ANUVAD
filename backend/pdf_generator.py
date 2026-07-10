import os

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from config import OUTPUT_FOLDER
from font_manager import get_font_by_text


def generate_pdf(
        translated_text,
        filename="translated_output.pdf"
):
    """
    Generate multilingual PDF while automatically
    selecting the correct font for each paragraph.
    """

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        filename
    )

    document = SimpleDocTemplate(
        output_path
    )

    styles = getSampleStyleSheet()

    style = styles["Normal"]

    style.leading = 20

    elements = []

    paragraphs = translated_text.split("\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if paragraph == "":
            elements.append(
                Spacer(1, 10)
            )
            continue

        # Automatically choose correct font
        style.fontName = get_font_by_text(paragraph)

        elements.append(
            Paragraph(
                paragraph,
                style
            )
        )

    document.build(elements)

    print("\n====================================")
    print(" PDF Generated Successfully")
    print("====================================")
    print(output_path)

    return output_path


if __name__ == "__main__":

    sample = """
This is an English sentence.

Artificial Intelligence is transforming healthcare.

भारत तेजी से विकास कर रहा है।

এই প্রকল্পটি সম্পূর্ণ অফলাইনে কাজ করে।

ଏହି ପ୍ରକଳ୍ପଟି ସମ୍ପୂର୍ଣ୍ଣ ଅଫଲାଇନ୍ ଭାବରେ କାମ କରେ।

ગુજરાતી ભાષા પણ સપોર્ટેડ છે.

ਪੰਜਾਬੀ ਵੀ ਸਮਰਥਿਤ ਹੈ।

இந்த திட்டம் இணையம் இல்லாமல் செயல்படுகிறது.

ఈ ప్రాజెక్ట్ పూర్తిగా ఆఫ్‌లైన్‌లో పనిచేస్తుంది.

ಈ ಯೋಜನೆ ಸಂಪೂರ್ಣ ಆಫ್‌ಲೈನ್‌ನಲ್ಲಿ ಕಾರ್ಯನಿರ್ವಹಿಸುತ್ತದೆ.

ഈ പദ്ധതി പൂർണ്ണമായും ഓഫ്‌ലൈനായി പ്രവർത്തിക്കുന്നു.
"""

    generate_pdf(sample)