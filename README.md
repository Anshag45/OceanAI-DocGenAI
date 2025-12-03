🌊 OceanAI-DocGenAI
AI-Assisted Document Authoring & Generation Platform

OceanAI-DocGenAI is a full-stack AI platform that generates, refines, and exports business documents in Word (.docx) and PowerPoint (.pptx) formats.
It features AI-driven content creation, a structured refinement workflow, and complete project/user management.

🚀 Features
🔹 AI-Powered Content Generation

Section-wise and slide-wise AI content

Optional AI-generated outlines

Uses Google Gemini for generation & refinement

🔹 Intelligent Refinement Workflow

Per-section refinement prompts

Like/Dislike feedback

Commenting + revision history

Persistent storage for all edits

🔹 Document Export

Clean, professional .docx export (python-docx)

Structured .pptx export (python-pptx)

Files stored automatically inside /exports/

🔹 User & Project Management

User registration & login

JWT-based authentication

Project dashboard

Document configuration (DOCX / PPTX)

🧩 Tech Stack
Frontend

React + TypeScript

Vite

Component-based architecture

REST API communication

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

2. Activate Environment

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Configure Environment Variables

Copy .env.example → .env and set:

GEMINI_API_KEY=<your_api_key>
GEMINI_MODEL=gemini-pro
SECRET_KEY=<jwt_secret>
DATABASE_URL=sqlite:///./app.db

5. Start Backend Server
uvicorn main:app --reload


API Documentation:
👉 http://localhost:8000/docs

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


Frontend runs at:
👉 http://localhost:3000

🔌 API Endpoints Overview
Auth Endpoints
Method	Route	Description
POST	/auth/register	User registration
POST	/auth/login	Login & get JWT
Project Endpoints
Method	Route	Description
POST	/project/create	Create a new project
POST	/project/{id}/generate	Generate AI document content
GET	/project/{id}	Fetch full project details
Refinement Endpoints
Method	Route	Description
POST	/refine	Refine specific section/slide
📤 Document Export

.docx export using python-docx

.pptx export using python-pptx

Files saved to:

/exports/

📌 Future Enhancements

Multi-language content generation

Advanced formatting presets

Real-time collaboration

Admin & analytics dashboard

Template-based export system

