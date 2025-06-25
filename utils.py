from fastapi import UploadFile, HTTPException
from PIL import Image
import io

SUPPORTED_TYPES = ["application/pdf", "image/jpeg"]

def validate_file(file: UploadFile):
    if file.content_type not in SUPPORTED_TYPES:
        raise HTTPException(status_code=400, detail="Unsupported file type. Use PDF or JPEG.")

def read_image_file(file: UploadFile) -> Image.Image:
    return Image.open(io.BytesIO(file.file.read()))

