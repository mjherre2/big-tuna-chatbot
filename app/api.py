from fastapi import APIRouter, UploadFile, File, Form
from app.logic import get_chat_response
from app.ingest import ingest_pdf

router = APIRouter()

@router.post("/chat")
async def chat(input: str):
    response = get_chat_response(input)
    return {"response": response}

@router.post("/upload")
async def upload(file: UploadFile = File(...)):
    ingest_pdf(file)
    return {"status": "uploaded"}