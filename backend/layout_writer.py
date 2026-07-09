import fitz
import os
import html

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

FONT_DIR = os.path.join(PROJECT_ROOT, "fonts")


def get_font_file(text):
    """
    Automatically select the correct font
    according to the translated language.
    """

    # Devanagari (Hindi, Marathi, Nepali, Sanskrit)
    if any("\u0900" <= ch <= "\u097F" for ch in text):
        return "NotoSansDevanagari-Regular.ttf"

    # Bengali / Assamese
    elif any("\u0980" <= ch <= "\u09FF" for ch in text):
        return "NotoSansBengali-Regular.ttf"

    # Gurmukhi (Punjabi)
    elif any("\u0A00" <= ch <= "\u0A7F" for ch in text):
        return "NotoSansGurmukhi-Regular.ttf"

    # Gujarati
    elif any("\u0A80" <= ch <= "\u0AFF" for ch in text):
        return "NotoSansGujarati-Regular.ttf"

    # Odia
    elif any("\u0B00" <= ch <= "\u0B7F" for ch in text):
        return "NotoSansOriya-Regular.ttf"

    # Tamil
    elif any("\u0B80" <= ch <= "\u0BFF" for ch in text):
        return "NotoSansTamil-Regular.ttf"

    # Telugu
    elif any("\u0C00" <= ch <= "\u0C7F" for ch in text):
        return "NotoSansTelugu-Regular.ttf"

    # Kannada
    elif any("\u0C80" <= ch <= "\u0CFF" for ch in text):
        return "NotoSansKannada-Regular.ttf"

    # Malayalam
    elif any("\u0D00" <= ch <= "\u0D7F" for ch in text):
        return "NotoSansMalayalam-Regular.ttf"

    # Arabic (Urdu)
    elif any("\u0600" <= ch <= "\u06FF" for ch in text):
        return "NotoSansArabic-Regular.ttf"

    # Ol Chiki (Santali)
    elif any("\u1C50" <= ch <= "\u1C7F" for ch in text):
        return "NotoSansOlChiki-Regular.ttf"

    # Default English
    return "NotoSans-Regular.ttf"


def write_text(page, block, translated_text):

    rect = fitz.Rect(block["bbox"])

    archive = fitz.Archive(FONT_DIR)

    font_size = 12

    if block["spans"]:
        font_size = block["spans"][0]["size"]

    font_file = get_font_file(translated_text)

    css = f"""
    @font-face {{
        font-family: customfont;
        src: url("{font_file}");
    }}

    body {{
        font-family: customfont;
        font-size: {font_size}px;
        color: black;
        margin: 0;
        padding: 0;
    }}
    """

    html_text = f"""
    <body>
        {html.escape(translated_text)}
    </body>
    """

    page.insert_htmlbox(
        rect,
        html_text,
        css=css,
        archive=archive
    )