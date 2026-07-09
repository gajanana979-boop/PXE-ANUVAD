from huggingface_hub import snapshot_download
import os

MODEL_NAME = "facebook/nllb-200-distilled-600M"

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(PROJECT_ROOT, "models", "nllb-200")

os.makedirs(MODEL_PATH, exist_ok=True)

print("Downloading model... Please wait.")

snapshot_download(
    repo_id=MODEL_NAME,
    local_dir=MODEL_PATH,
    local_dir_use_symlinks=False
)

print("\nDownload completed successfully!")
print("Model saved at:")
print(MODEL_PATH)