OceanAI-DocGenAI
AI-Assisted Document Authoring & Generation Platform

OceanAI-DocGenAI is a full-stack application for generating, refining, and exporting structured business documents using AI.
The system supports both Word (.docx) and PowerPoint (.pptx) formats and provides a guided workflow from document configuration to export.

🚀 Features
AI-Powered Content Generation

Section-wise (DOCX) and slide-wise (PPTX) content generation

Uses Google Gemini for generation and refinement

Optional AI-generated outlines

Refinement Workflow

Per-section refinement prompts

Like/Dislike feedback

Commenting and revision history

Persistent storage of all edits

Document Export

Exports to .docx using python-docx

Exports to .pptx using python-pptx

Clean structured formatting

User & Project Management

User registration and login

JWT authentication

Dashboard with all projects

Project configuration (DOCX/PPTX)

🧩 Tech Stack
Frontend

React + TypeScript

Vite / Modern component structure

REST API communication

Backend

FastAPI

Google Gemini API

SQLAlchemy ORM

python-docx & python-pptx

Database

SQLite (configurable to PostgreSQL)

📂 Project Structure
OceanAI-DocGenAI/
│
├── backend/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── requirements.txt
│   ├── .env.example
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── project_router.py
│   │   └── refine_router.py
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── export_docx.py
│   │   └── export_pptx.py
│   └── utils/
│       └── jwt_handler.py
│
└── frontend/
    ├── src/
    ├── components/
    ├── pages/
    ├── package.json
    └── vite.config.ts

⚙️ Backend Setup
1. Create Virtual Environment
cd backend
python -m venv venv


Activate:

Windows

venv\Scripts\activate


Linux/Mac

source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables

Copy .env.example → .env

GEMINI_API_KEY=<your_api_key>
GEMINI_MODEL=gemini-pro
SECRET_KEY=<jwt_secret>
DATABASE_URL=sqlite:///./app.db

4. Run Backend Server
uvicorn main:app --reload


API Docs:
http://localhost:8000/docs

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


Runs at:
http://localhost:3000

🔌 API Endpoints Overview
Auth
Method	Route	Description
POST	/auth/register	User registration
POST	/auth/login	Login and receive JWT
Project
Method	Route	Description
POST	/project/create	Create a project
POST	/project/{id}/generate	Generate AI content
GET	/project/{id}	Fetch project details
Refinement
Method	Route	Description
POST	/refine	Refine section content
📤 Exporting Documents

DOCX files generated using python-docx

PPTX files generated using python-pptx

Exports stored in /exports/ directory

