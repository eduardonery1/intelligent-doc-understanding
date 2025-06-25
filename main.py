from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from ocr import OCR
from vector_db import VectorDB
from schema import EntityExtractionResponse
from utils import validate_file, read_image_file
from llm_extraction import parse_entities
from dotenv import load_dotenv
import logging
import time

load_dotenv()
app = FastAPI()
ocr_engine = None
vector_db = None


@app.on_event("startup")
def load_resources():
    global ocr_engine, vector_db
    ocr_engine = OCR()
    vector_db = VectorDB()
    logging.info("OCR and VectorDB initialized.")

@app.post("/extract_entities", response_model=EntityExtractionResponse)
async def extract_entities(file: UploadFile = File(...)):
    start = time.time()
    try:
        validate_file(file)
        if file.content_type == "application/pdf":
            content = await file.read()
            text = ocr_engine.extract_text_from_pdf(content)
        elif file.content_type == "image/jpeg":
            image = read_image_file(file)
            text = ocr_engine.extract_text_from_image(image)
        else:
            raise HTTPException(status_code=415, detail="Unsupported Media Type")

        if not text.strip():
            raise HTTPException(status_code=422, detail="No readable text found")

        doc_type, confidence = vector_db.predict_type(text)

        entities = parse_entities(doc_type, text)

        return EntityExtractionResponse(
            document_type=doc_type,
            confidence=round(confidence, 3),
            extracted_text=text[:1000],  # limit size for safety
            entities=entities,
            processing_time=f"{time.time() - start:.2}s"
        )

    except Exception as e:
        logging.exception("Error processing file.")
        raise HTTPException(status_code=500, detail=f"Processing error: {str(e)}")

