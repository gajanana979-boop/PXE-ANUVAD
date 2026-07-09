import os
import re

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

FONT_DIR = os.path.join(PROJECT_ROOT, "fonts")


FONT_FILES = {

    "english": "NotoSans-Regular.ttf",

    "devanagari": "NotoSansDevanagari-Regular.ttf",

    "bengali": "NotoSansBengali-Regular.ttf",

    "gujarati": "NotoSansGujarati-Regular.ttf",

    "gurmukhi": "NotoSansGurmukhi-Regular.ttf",

    "odia": "NotoSansOriya-Regular.ttf",

    "tamil": "NotoSansTamil-Regular.ttf",

    "telugu": "NotoSansTelugu-Regular.ttf",

    "kannada": "NotoSansKannada-Regular.ttf",

    "malayalam": "NotoSansMalayalam-Regular.ttf",

    "arabic": "NotoSansArabic-Regular.ttf",

    "olchiki": "NotoSansOlChiki-Regular.ttf"

}


def get_font_by_text(text):

    if re.search(r'[\u0900-\u097F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["devanagari"])

    if re.search(r'[\u0980-\u09FF]', text):
        return os.path.join(FONT_DIR, FONT_FILES["bengali"])

    if re.search(r'[\u0A00-\u0A7F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["gurmukhi"])

    if re.search(r'[\u0A80-\u0AFF]', text):
        return os.path.join(FONT_DIR, FONT_FILES["gujarati"])

    if re.search(r'[\u0B00-\u0B7F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["odia"])

    if re.search(r'[\u0B80-\u0BFF]', text):
        return os.path.join(FONT_DIR, FONT_FILES["tamil"])

    if re.search(r'[\u0C00-\u0C7F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["telugu"])

    if re.search(r'[\u0C80-\u0CFF]', text):
        return os.path.join(FONT_DIR, FONT_FILES["kannada"])

    if re.search(r'[\u0D00-\u0D7F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["malayalam"])

    if re.search(r'[\u0600-\u06FF]', text):
        return os.path.join(FONT_DIR, FONT_FILES["arabic"])

    if re.search(r'[\u1C50-\u1C7F]', text):
        return os.path.join(FONT_DIR, FONT_FILES["olchiki"])

    return os.path.join(FONT_DIR, FONT_FILES["english"])