import re
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from config import MODEL_PATH, DEVICE, MAX_NEW_TOKENS
from languages import LANGUAGE_CODES
ACRONYM_MAP = {

    "DRDO": "डीआरडीओ",
    "PXE": "पीएक्सई",
    "ANUVAD": "अनुवाद",
    "ISRO": "इसरो",
    "NASA": "नासा",
    "AI": "एआई",
    "ML": "एमएल",
    "NLP": "एनएलपी",
    "PDF": "पीडीएफ",
    "CPU": "सीपीयू",
    "GPU": "जीपीयू"

}


print("Loading NLLB tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

print("Loading NLLB model...")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_PATH)

model.to(DEVICE)

print("\nNLLB Translation Engine Ready!\n")




def remove_duplicate_words(text):
    """
    Remove consecutive duplicate words.
    Example:
    अनुवाद अनुवाद -> अनुवाद
    """

    words = text.split()

    cleaned = []

    for word in words:

        if not cleaned or cleaned[-1] != word:
            cleaned.append(word)

    return " ".join(cleaned)
def transliterate_remaining_english(text):
    """
    Replace known acronyms after translation.
    """

    pattern = r"\b[A-Za-z]+\b"

    def replace(match):
        word = match.group()

        if word.upper() in ACRONYM_MAP:
            return ACRONYM_MAP[word.upper()]

        return word

    return re.sub(pattern, replace, text)

def translate(text, source_language, target_language):
    """
    Translate text from source language to target language.
    """

    if not text.strip():
        return ""

    if source_language not in LANGUAGE_CODES:
        raise ValueError(
            f"Unsupported source language: {source_language}"
        )

    if target_language not in LANGUAGE_CODES:
        raise ValueError(
            f"Unsupported target language: {target_language}"
        )

    if source_language == target_language:
        return text
    # Replace known acronyms BEFORE translation
    for eng, native in ACRONYM_MAP.items():
        text = re.sub(
        rf"\b{re.escape(eng)}\b",
        native,
        text,
        flags=re.IGNORECASE
    )

    tokenizer.src_lang = LANGUAGE_CODES[source_language]

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        max_length=512
    )

    inputs = {
        key: value.to(DEVICE)
        for key, value in inputs.items()
    }

    translated_tokens = model.generate(
        **inputs,
        forced_bos_token_id=tokenizer.convert_tokens_to_ids(
            LANGUAGE_CODES[target_language]
        ),
        max_new_tokens=MAX_NEW_TOKENS
    )

    translated_text = tokenizer.batch_decode(
    translated_tokens,
    skip_special_tokens=True
    )[0]

    translated_text = transliterate_remaining_english(
    translated_text
   )

    translated_text = remove_duplicate_words(
    translated_text
    )

    return translated_text


if __name__ == "__main__":

    print("=" * 60)
    print("Offline Multilingual Translator")
    print("=" * 60)

    text = input("\nEnter Text:\n").strip()

    source = input("\nSource Language: ").strip()

    target = input("\nTarget Language: ").strip()

    try:

        result = translate(
            text,
            source,
            target
        )

        print("\n")
        print("=" * 60)
        print("Translated Output")
        print("=" * 60)
        print(result)

    except Exception as error:

        print("\nError:")
        print(error)