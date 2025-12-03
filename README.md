🌊 OceanAI-DocGenAI
AI-Assisted Document Authoring & Generation Platform

OceanAI-DocGenAI is a full-stack, end-to-end platform for generating, refining, and exporting business documents using AI.
It supports Word (.docx) and PowerPoint (.pptx) generation, provides a guided refinement workflow, and includes complete project/user management.

🚀 Features
AI-Powered Content Generation

Slide-wise / section-wise content generation

Optional AI-generated document outlines

Powered by Google Gemini

Automated content refinement and regeneration

Refinement Workflow

Per-section refinement prompts

Like/Dislike feedback

Commenting system

Revision history

Persistent storage of all edits in database

Document Export

Export to .docx using python-docx

Export to .pptx using python-pptx

Clean, structured formatting tailored for business use

User & Project Management

User registration and login

JWT-based authentication

Dashboard with all saved projects

Choice of document type (DOCX / PPTX)

Full project configuration flow

🧩 Tech Stack
Frontend

React + TypeScript

Vite

Component-based modern UI architecture

REST API integration

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

Activate

Windows

venv\Scripts\activate


Linux / Mac

source venv/bin/activate

2. Install Dependencies
pip install -r requirements.txt

3. Configure Environment Variables

Copy .env.example → .env and update:

GEMINI_API_KEY=<your_api_key>
GEMINI_MODEL=gemini-pro
SECRET_KEY=<jwt_secret>
DATABASE_URL=sqlite:///./app.db

4. Run Backend Server
uvicorn main:app --reload


API Docs available at:
👉 http://localhost:8000/docs

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


Runs at:
👉 http://localhost:3000

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
POST	/refine	Refine content section/slide
📤 Document Export

.docx generated using python-docx

.pptx generated using python-pptx

Exports saved in:

/exports/

📌 Future Enhancements (Optional Section)

Multi-language document generation

Collaboration mode

Custom styling presets for PPTX/DOCX

Role-based access control

Admin dashboard
