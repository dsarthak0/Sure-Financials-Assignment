from fastapi import FastAPI, UploadFile, File
import shutil
import os


from utils.pdf_reader import extract_text
from utils.issuer_detector import detect_issuer
from parsers.generic_parser import GenericCardParser

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


parser = GenericCardParser()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/parse")
async def parse_statement(file: UploadFile = File(...)):
    # Save uploaded PDF
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = extract_text(file_path)

    # Detect card issuer
    issuer = detect_issuer(text)
    if not issuer:
        return {"error": "Unsupported issuer"}

    # Parse statement
    result = parser.parse(text, issuer)

    return result
