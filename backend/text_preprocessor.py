import re


def clean_text(text):
    """
    Clean extracted text before translation.
    """

    if not text:
        return ""

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([.,!?;:])", r"\1", text)

    # Remove invisible characters
    text = text.replace("\u00A0", " ")
    text = text.replace("\u200B", "")

    # Trim
    text = text.strip()

    return text


if __name__ == "__main__":

    sample = """
    This    is    a      sample     text.

    It      contains      extra     spaces.
    """

    print(clean_text(sample))