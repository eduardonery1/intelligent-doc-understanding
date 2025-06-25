from typing import List, Optional, Union
from pydantic import BaseModel
from typing import Optional


class EntityExtractionResponse(BaseModel):
    document_type: str
    confidence: float
    entities: object
    processing_time: str

class Advertisement(BaseModel):
    title: Optional[str]
    product_or_service: Optional[str]
    price: Optional[str]
    contact_information: Optional[str]
    date: Optional[str]
    call_to_action: Optional[str]


class Budget(BaseModel):
    budget_name: Optional[str]
    department: Optional[str]
    fiscal_year: Optional[str]
    total_budget: Optional[str]
    expenditures: Optional[str]
    remaining_balance: Optional[str]


class Email(BaseModel):
    sender: Optional[str]
    recipient: Optional[str]
    subject: Optional[str]
    date: Optional[str]
    body: Optional[str]


class FileFolder(BaseModel):
    folder_name: Optional[str]
    document_titles: Optional[List[str]]
    creation_date: Optional[str]
    owner: Optional[str]


class Form(BaseModel):
    form_title: Optional[str]
    form_id: Optional[str]
    submission_date: Optional[str]
    fields_filled: Optional[dict]
    signatures: Optional[List[str]]


class Handwritten(BaseModel):
    author: Optional[str]
    date: Optional[str]
    content: Optional[str]


class Invoice(BaseModel):
    invoice_number: Optional[str]
    vendor_name: Optional[str]
    client_name: Optional[str]
    date: Optional[str]
    due_date: Optional[str]
    total_amount: Optional[str]
    item_list: Optional[List[str]]


class Letter(BaseModel):
    sender: Optional[str]
    recipient: Optional[str]
    date: Optional[str]
    subject: Optional[str]
    body: Optional[str]
    signature: Optional[str]


class Memo(BaseModel):
    sender: Optional[str]
    recipient: Optional[str]
    date: Optional[str]
    subject: Optional[str]
    body: Optional[str]


class NewsArticle(BaseModel):
    headline: Optional[str]
    author: Optional[str]
    publication_date: Optional[str]
    location: Optional[str]
    content: Optional[str]


class Presentation(BaseModel):
    title: Optional[str]
    author: Optional[str]
    date: Optional[str]
    slide_titles: Optional[List[str]]
    key_points: Optional[List[str]]


class Questionnaire(BaseModel):
    title: Optional[str]
    creator: Optional[str]
    questions: Optional[List[str]]
    response_type: Optional[str]
    submission_date: Optional[str]


class Resume(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    skills: Optional[List[str]]
    education: Optional[List[str]]
    work_experience: Optional[List[str]]
    certifications: Optional[List[str]]


class ScientificPublication(BaseModel):
    title: Optional[str]
    authors: Optional[List[str]]
    abstract: Optional[str]
    keywords: Optional[List[str]]
    publication_date: Optional[str]
    journal_name: Optional[str]
    doi: Optional[str]


class ScientificReport(BaseModel):
    report_title: Optional[str]
    authors: Optional[List[str]]
    abstract: Optional[str]
    introduction: Optional[str]
    methodology: Optional[str]
    results: Optional[str]
    conclusion: Optional[str]
    date: Optional[str]


class Specification(BaseModel):
    spec_name: Optional[str]
    version: Optional[str]
    author: Optional[str]
    date: Optional[str]
    requirements: Optional[List[str]]
    use_cases: Optional[List[str]]

