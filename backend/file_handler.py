import os

from config import INPUT_FOLDER
from config import OUTPUT_FOLDER


SUPPORTED_IMAGE_TYPES = [
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp",
    ".tif",
    ".tiff"
]

SUPPORTED_PDF_TYPES = [
    ".pdf"
]


def initialize_folders():
    """
    Create input and output folders if they do not exist.
    """

    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)


def file_exists(file_path):
    """
    Check if file exists.
    """

    return os.path.isfile(file_path)


def get_file_extension(file_path):
    """
    Returns file extension.
    """

    return os.path.splitext(file_path)[1].lower()


def get_file_type(file_path):
    """
    Detect whether file is PDF or IMAGE.
    """

    extension = get_file_extension(file_path)

    if extension in SUPPORTED_PDF_TYPES:
        return "PDF"

    if extension in SUPPORTED_IMAGE_TYPES:
        return "IMAGE"

    return "UNSUPPORTED"


def validate_file(file_path):
    """
    Validate uploaded file.
    """

    if not file_exists(file_path):
        raise FileNotFoundError(
            f"File not found: {file_path}"
        )

    file_type = get_file_type(file_path)

    if file_type == "UNSUPPORTED":
        raise ValueError(
            "Unsupported file type."
        )

    return file_type


if __name__ == "__main__":

    initialize_folders()

    path = input("Enter file path: ").strip()

    try:

        file_type = validate_file(path)

        print("\nFile is valid.")
        print("Detected Type:", file_type)

    except Exception as error:

        print("\nError:")
        print(error)