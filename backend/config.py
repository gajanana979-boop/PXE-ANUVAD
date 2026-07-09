import os

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    PROJECT_ROOT,
    "models",
    "nllb-200"
)

INPUT_FOLDER = os.path.join(
    PROJECT_ROOT,
    "input"
)

OUTPUT_FOLDER = os.path.join(
    PROJECT_ROOT,
    "output"
)

DEVICE = "cpu"

MAX_NEW_TOKENS = 512
