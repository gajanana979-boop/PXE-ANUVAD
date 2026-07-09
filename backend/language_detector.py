import os
import fasttext


# -------------------------------------------------
# Load FastText Language Detection Model
# -------------------------------------------------

MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "lid.176.bin"
)

model = fasttext.load_model(MODEL_PATH)


# -------------------------------------------------
# FastText Language Code -> Project Language Name
# -------------------------------------------------

LANGUAGE_MAP = {

    # English
    "en": "English",

    # Major Indian Languages
    "hi": "Hindi",
    "bn": "Bengali",
    "or": "Odia",
    "ta": "Tamil",
    "te": "Telugu",
    "ml": "Malayalam",
    "kn": "Kannada",
    "mr": "Marathi",
    "gu": "Gujarati",
    "pa": "Punjabi",
    "ur": "Urdu",
    "as": "Assamese",
    "ne": "Nepali",
    "sd": "Sindhi",

    # Additional Indian Languages
    "ks": "Kashmiri",
    "mai": "Maithili",
    "doi": "Dogri",
    "gom": "Konkani",
    "brx": "Bodo",
    "mni": "Manipuri",
    "sat": "Santali",

    # Classical Language
    "sa": "Sanskrit"
}


# -------------------------------------------------
# Detect Language
# -------------------------------------------------

def detect_language(text):
    """
    Detect language from text using FastText.

    Parameters
    ----------
    text : str

    Returns
    -------
    str
        Language name.
    """

    if not text:
        return "Unknown"

    text = text.strip()

    if text == "":
        return "Unknown"

    prediction = model.predict(
        text.replace("\n", " "),
        k=1
    )

    language_code = prediction[0][0].replace(
        "__label__",
        ""
    )

    return LANGUAGE_MAP.get(
        language_code,
        "Unknown"
    )


# -------------------------------------------------
# Test
# -------------------------------------------------

if __name__ == "__main__":

    print("=" * 60)
    print("Automatic Language Detection")
    print("=" * 60)

    while True:

        text = input("\nEnter Text (type 'exit' to quit): ")

        if text.lower() == "exit":
            break

        language = detect_language(text)

        print(f"\nDetected Language : {language}")