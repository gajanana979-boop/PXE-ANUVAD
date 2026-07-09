def map_font(original_font):

    original_font = original_font.lower()

    if "bold" in original_font:
        return "bold"

    if "italic" in original_font or "oblique" in original_font:
        return "italic"

    return "regular"