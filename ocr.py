import easyocr
from pdf2image import convert_from_bytes
from PIL import Image
import numpy as np
import io

class OCR:
    def __init__(self):
        self.reader = easyocr.Reader(['en'], gpu=True)

    def extract_text_from_image(self, image: Image.Image) -> str:
        results = self.reader.readtext(np.array(image), detail=0)
        return "\n".join(results)

    def extract_text_from_pdf(self, pdf_bytes: bytes) -> str:
        images = convert_from_bytes(pdf_bytes)
        text = ""
        for img in images:
            text += self.extract_text_from_image(img) + "\n"
        return text.strip()

