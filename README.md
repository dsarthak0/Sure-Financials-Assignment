# Sure-Financials-Assignment
📄 Credit Card Statement Parser
A web-based application that parses credit card PDF statements from multiple banks and extracts key information such as card details, billing cycle, due date, and total amount due.

Features:

  Supports 5 major credit card issuers:
  
  HDFC
  
  ICICI
  
  Axis
  
  SBI
  
  Amex
  
Extracts 5 key data points:

  Handles real-world PDF formats
  
  Backend built with FastAPI
  
  Frontend built with React
  
  Modular, scalable parser design

🛠️ Tech Stack

  Backend
  
     Python
     FastAPI
     pdfplumber
     Uvicorn
  Frontend
  
     React (Vite)
     Fetch API
     
📁 Project Structure

ccparser/
│
├── app.py

├── parser/
│   ├── generic_parser.py
│   └── bank_patterns.py
│
├── utils/
│   ├── pdf_reader.py
│   └── issuer_detector.py
│
├── uploads/
├── venv/
├── requirements.txt
│
└── frontend/
    ├── src/
    ├── package.json
    └── index.html
    
⚙️ Backend Setup (FastAPI)

   1️⃣ Navigate to backend folder
    cd ccparser
    
   2️⃣ Create virtual environment
    python3 -m venv venv
    
   3️⃣ Activate virtual environment
   source venv/bin/activate
   
   4️⃣ Install dependencies
   pip install fastapi uvicorn pdfplumber python-multipart
   
   5️⃣ Run backend server
   python -m uvicorn app:app --reload
   
   Backend will run at:
    http://127.0.0.1:8000
    
   API docs:
    http://127.0.0.1:8000/docs
    
🎨 Frontend Setup (React)

   1️⃣ Navigate to frontend
    cd frontend
    
   2️⃣ Install dependencies
   npm install
   
   3️⃣ Run React app
   npm start
   
   Frontend will run at:
   http://localhost:3000
   
🔗 CORS Configuration
Backend includes CORS support for React frontend:
allow_origins=["http://localhost:3000"]

🧪 How to Use

Open the React app in browser

Upload a credit card statement PDF

Click Upload & Parse

View extracted details in JSON format

📤 Sample Output
{

  "issuer": "HDFC",
  
  "last_4_digits": "1234",
  
  "billing_cycle": "01 Nov 2024 - 30 Nov 2024",
  
  "due_date": "15 Dec 2024",
  
  "total_due": "24580"
}

🧠 Design Approach

Extract text from PDF

Detect issuer using keyword matching

Use a generic parser with bank-specific regex configurations

Easily extensible for new banks


👨‍💻 Author
Sarthak Dhanvate
