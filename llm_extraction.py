from google import genai
from dotenv import load_dotenv
from schema import *
import os
import json


load_dotenv()

DOCUMENT_CLASS_MAP = {
    "advertisement": Advertisement,
    "budget": Budget,
    "email": Email,
    "file_folder": FileFolder,
    "form": Form,
    "handwritten": Handwritten,
    "invoice": Invoice,
    "letter": Letter,
    "memo": Memo,
    "news_article": NewsArticle,
    "presentation": Presentation,
    "questionnaire": Questionnaire,
    "resume": Resume,
    "scientific_publication": ScientificPublication,
    "scientific_report": ScientificReport,
    "specification": Specification
}


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def parse_entities(document_type: str, text: str) -> dict:
    schema = DOCUMENT_CLASS_MAP.get(document_type.lower(), [])

    prompt = f"""
Given the following text extracted from a document of type "{document_type}",
extract these fields: {schema.__fields__}.
Return your response as a valid JSON object with no additional text.

Document Text:
{text}
    """.strip()

    try:
        response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt, 
                    config = {"response_mime_type": "application/json",
                              "response_schema": schema
                            }
                    )
        content = response.text.strip()
        return json.loads(content) # Replace with json.loads(content) if model is consistent
    except Exception as e:
        return {"error": f"LLM extraction failed: {str(e)}"}

