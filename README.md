# Intelligent Document Understanding API

## Overview

This project implements an end-to-end document processing API that combines OCR technology, vector database retrieval, and large language models to extract structured information from unstructured documents. The system can process both PDF and image documents, classify them by type, and extract relevant entities using LLMs.

## Key Features

- Supports PDF and JPEG document uploads
- Optical Character Recognition (OCR) using EasyOCR
- Document type classification using FAISS vector database
- Entity extraction using Gemini LLM
- FastAPI-based REST endpoint
- Standardized JSON response format

## System Architecture

```
┌─────────────┐   ┌─────────────┐   ┌────────────────┐   ┌─────────────┐
│  Document   │ → │    OCR      │ → │  Document Type │ → │   Entity    │
│  Upload     │   │ Processing  │   │ Classification │   │ Extraction  │
└─────────────┘   └─────────────┘   └────────────────┘   └─────────────┘
```

## Installation

### Prerequisites

- Python 3.8+
- GPU (recommended for OCR performance)
- Google Gemini API key (for entity extraction)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/eduardonery1/intelligent-doc-understanding.git
   cd intelligent-doc-understanding
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   ```

3. Install dependencies:
   ```bash
   conda install faiss-gpu
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

5. Prepare the vector database:
   - Place your training documents in a `docs-sm` folder downloaded from this link https://www.kaggle.com/datasets/shaz13/real-world-documents-collections
   - Run the vector store builder:
     ```bash
     python vector_store.py
     ```
   - You all also download the generated data with git-lfs
   ```bash
     git lfs pull
   ```

## API Usage

### Running the Server

Start the FastAPI server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Endpoint

**POST `/extract_entities`**

Extracts text, classifies document type, and identifies entities from uploaded documents.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- Body: file (PDF or JPEG document)

**Response:**
```json
{
  "document_type": "email",
  "confidence": 1,
  "entities": {
    "sender": "Elves Robert G",
    "recipient": "Zimmeriarn Mike, Patskan, Seorge, Rustemeler, Klaus, Roemer, Ewald",
    "subject": "RE: Alternate puff profiles",
    "date": "Wednesday, October 30, 2002 10.26 AM",
    "body": "Mkke Your group certainly in the oop We need discuss having your tolks run the metals analysis Ot the JLI under thc exaggeratcd conditions Ucas Ihc GCIMS Fingcrprinting of particulalc an GVP from JLI allcmate , could use the whole smoke puff by puff analysis_ Im not familiar with the puff to puff work_ but if you think provide more inforration, we are interested: Bill Gardner did the previous GCIMS Fingerprinting work to determine the serni-quantitative dlfferences belween the Caco3 and AMP smokes In the EHCSS; Possibly BilI could corpare Ihe differences two phases with puffing condilions: Give me call; (Rest regards, Robbie 'Elrs Original Message - From: Zimnmemann, Mike Sent: Tuesday October 29 2002 4.10 PM To: Elves, Robert Subject: Altcrnalc protilcs lhanks. please kccp me posted olhcr data relaled this_ and Iel me know good lime get together t0 g0 over what we discussed this morning, thanks Onigina e98ede Etl Dal Sent: Tuescjy Ocober 29.202 Patsker Rolnei Exald Ruseneier Klau:' Wrenm Zinn Eimann Uke Sublect; FW: Aternare FU \" Pro iles Everyone Bill Rickert at Labslal sent Ihls me wilth regard their experience and ability t0 perform alt puff profiles their machines_ FYI with regard t0 Our effons on the \"JLI-TOPOCRAPHY\" Study. 'Best Robbie 'Eltes Original Messuge From: Williamn Rickent Sent: Monday. October 28, 2002 12.51 PM To: Robent Elves@pmusa com Subject: Alternale puti proliles Robbie based on the reponse from Pete (SB8 allached) We should be able work within the range of parameters of interest. Billl Message: Fwd RE: Quole Requesl (Morris M29) E2067475360 pulf Frcm . 6g regards,"
  },
  "processing_time": "1.3e+01s"
}
```

**Example Request (curl):**
```bash
curl -X POST -F "file=@document.pdf" http://localhost:8000/extract_entities
```

## Testing

The API can be tested using:
1. Direct curl commands as shown above
2. FastAPI's built-in Swagger UI at `http://localhost:8000/docs`
3. Postman or similar API testing tools

## Configuration

Key configuration options:

- **OCR Settings**: Modify `ocr.py` to change language support or OCR parameters
- **Vector Database**: Adjust embedding model in `vector_db.py` (default: 'all-MiniLM-L6-v2')
- **LLM Settings**: Configure prompt templates and model selection in `llm_extraction.py`

## Project Structure

```
.
├── main.py                # FastAPI application entry point
├── ocr.py                 # OCR processing module
├── vector_db.py           # Vector database operations
├── vector_store.py        # Vector index creation
├── llm_extraction.py      # LLM-based entity extraction
├── schema.py              # Pydantic models and response schemas
├── utils.py               # Utility functions
└── docs-sm/               # Sample documents for vector database
```

## Troubleshooting

1. **OCR Errors**: Ensure CUDA is properly configured if using GPU acceleration
2. **Vector Database Issues**: Verify documents are properly organized in `docs-sm`
3. **LLM Failures**: Check your API key and internet connection

## Future Enhancements

- Support for additional document types
- Improved error handling for low-quality OCR results
- Confidence scoring for extracted entities
- Docker containerization
- Web interface for testing

