🌊 OceanAI-DocGenAI
AI-Assisted Document Authoring & Generation Platform

OceanAI-DocGenAI is a full-stack AI platform that generates, refines, and exports business documents in Word (.docx) and PowerPoint (.pptx) formats.
The system provides intelligent content generation, a refinement workflow, and complete user/project management.

🚀 Features
🔹 AI-Powered Content Generation

Section-wise and slide-wise content generation

Supports AI-generated document outlines

Uses Google Gemini for generation and refinement

🔹 Smart Refinement Workflow

Per-section refinement prompts

Like/Dislike feedback

Commenting and revision history

Persistent version storage

🔹 Document Export

.docx export using python-docx

.pptx export using python-pptx

Clean, structured formatting

Files saved inside /exports/ directory

🔹 User & Project Management

User registration & login

JWT-based authentication

Project dashboard

Select document type (DOCX or PPTX)

🧩 Tech Stack
Frontend

React

TypeScript

Vite

Backend

FastAPI

Google Gemini API

SQLAlchemy ORM

python-docx & python-pptx

JWT authentication

Database

SQLite (default)

Easily configurable to PostgreSQL

📂 Project Structure



OceanAI-DocGenAI/
├── backend/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── requirements.txt
│ ├── .env.example
│ ├── routers/
│ │ ├── auth_router.py
│ │ ├── project_router.py
│ │ └── refine_router.py
│ ├── services/
│ │ ├── ai_service.py
│ │ ├── export_docx.py
│ │ └── export_pptx.py
│ └── utils/
│ └── jwt_handler.py
│
└── frontend/
├── src/
├── components/
├── pages/
├── package.json
└── vite.config.ts





⚙️ Backend Setup
1. Navigate to backend & create virtual environment
cd backend
python -m venv venv

2. Activate the environment

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3. Install requirements
pip install -r requirements.txt

4. Create and configure .env

Copy .env.example → .env and fill:

GEMINI_API_KEY=<your_api_key>
GEMINI_MODEL=gemini-pro
SECRET_KEY=<jwt_secret>
DATABASE_URL=sqlite:///./app.db

5. Run backend
uvicorn main:app --reload


API Documentation:
👉 http://localhost:8000/docs

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


Runs on:
👉 http://localhost:3000

🔌 API Endpoints
Auth
Method	Route	Description
POST	/auth/register	Register user
POST	/auth/login	Login & receive JWT
Project
Method	Route	Description
POST	/project/create	Create project
POST	/project/{id}/generate	Generate AI content
GET	/project/{id}	Get project details
Refinement
Method	Route	Description
POST	/refine	Refine content
📤 Document Export

DOCX export using python-docx

PPTX export using python-pptx

Files stored under:

/exports/

🧭 Future Enhancements

Multi-language document generation

Template-based exports

Admin dashboard

Team collaboration mode

Advanced PPTX themes
