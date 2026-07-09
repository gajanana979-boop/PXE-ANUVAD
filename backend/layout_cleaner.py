import fitz


def add_redaction(page, bbox):
    """
    Add a redaction annotation only.
    Do NOT apply it here.
    """

    rect = fitz.Rect(bbox)

    page.add_redact_annot(
        rect,
        fill=(1, 1, 1)
    )


def apply_redactions(page):
    """
    Apply all redactions on this page.
    """

    page.apply_redactions()