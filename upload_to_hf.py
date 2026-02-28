from huggingface_hub import HfApi
import os

# Login to Hugging Face (you'll need your token)
# Get token from: https://huggingface.co/settings/tokens
# Run this once: huggingface-cli login

api = HfApi()

# Your space info
username = "MSK9218"
space_name = "MSK-Pdf-to-Excel-v1"

# Files to upload (exclude unnecessary ones)
files_to_upload = [
    "app.py",
    "requirements.txt",
    "Dockerfile",
    "README.md",
    "templates/index.html",
    "static/style.css",
]

# Upload each file
print("Uploading files to Hugging Face Space...")
for file_path in files_to_upload:
    if os.path.exists(file_path):
        try:
            api.upload_file(
                path_or_fileobj=file_path,
                path_in_repo=file_path,
                repo_id=f"{username}/{space_name}",
                repo_type="space",
            )
            print(f"✓ Uploaded: {file_path}")
        except Exception as e:
            print(f"✗ Failed {file_path}: {e}")
    else:
        print(f"✗ Not found: {file_path}")

print("\nUpload complete!")
print(f"Visit: https://huggingface.co/spaces/{username}/{space_name}")
