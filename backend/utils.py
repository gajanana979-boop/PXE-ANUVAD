import os
from datetime import datetime


def generate_output_filename(input_path, target_language):
    """
    Generate output PDF filename.
    """

    filename = os.path.splitext(
        os.path.basename(input_path)
    )[0]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    return f"{filename}_{target_language}_{timestamp}.pdf"


def ensure_directory(directory):

    os.makedirs(directory, exist_ok=True)