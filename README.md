🌊 OceanAI-DocGenAI
AI-Assisted Document Authoring & Generation Platform

OceanAI-DocGenAI is a full-stack AI application that allows users to create structured business documents using AI (Gemini).
Users can generate, refine, and export documents in DOCX and PPTX formats through an intuitive web interface.

✨ Built for the assignment:
Login → Configure → Generate → Refine → Export

🚀 Features
🔐 Authentication

User Registration

Login

JWT-based secure routes

📁 Project Management

Create DOCX or PPTX projects

Add section headers / slide titles

Dashboard to view all projects

🤖 AI Content Generation (Gemini)

Section-wise content generation

Slide-wise content generation

Optional AI-suggested outline

All data persisted in database

✏️ Refinement Interface

Refinement prompt per section/slide

Like / Dislike feedback

Comments stored in DB

Multiple refinement cycles

📤 Export

Export Word (.docx) using python-docx

Export PowerPoint (.pptx) using python-pptx

Clean formatting and proper structure

🧩 Tech Stack
Frontend

React + TypeScript

Tailwind & Component-based UI

Fetch API to interact with backend

Backend

FastAPI

Gemini (Google Generative AI)

SQLAlchemy ORM

JWT Authentication

python-docx + python-pptx

Database

SQLite (can be swapped with PostgreSQL)

📂 Folder Structure
OceanAI-DocGenAI/
│
│── backend/
│     ├── main.py
│     ├── database.py
│     ├── models.py
│     ├── schemas.py
│     ├── requirements.txt
│     ├── .env.example
│     ├── routers/
│     ├── services/
│     └── utils/
│
│── frontend/
│     ├── src/
│     ├── components/
│     ├── pages/
│     ├── package.json
│     └── ...
│
└── README.md

⚙️ Backend Setup (FastAPI + Gemini)
1. Create Virtual Environment
cd backend
python -m venv venv


Activate:

Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

2. Install Requirements
pip install -r requirements.txt

3. Add Environment Variables

Copy .env.example → .env

GEMINI_API_KEY=your_real_api_key
GEMINI_MODEL=gemini-pro
SECRET_KEY=super-secret-key
DATABASE_URL=sqlite:///./app.db

4. Run Server
uvicorn main:app --reload


Backend runs at:
👉 http://localhost:8000

Swagger API Docs:
👉 http://localhost:8000/docs

🖥️ Frontend Setup
cd frontend
npm install
npm run dev


or (depending on your setup):

pnpm install
pnpm dev


Frontend runs at:
👉 http://localhost:3000

🔌 Connecting Frontend & Backend

Update your frontend .env or API config with:

VITE_API_URL=http://localhost:8000

📡 API Endpoints Overview
Auth
Method	Route	Purpose
POST	/auth/register	Register user
POST	/auth/login	Login + JWT
Projects
Method	Route	Purpose
POST	/project/create	Create project
POST	/project/{id}/generate	Generate AI content
GET	/project/{id}	Fetch project
Refinement
Method	Route	Purpose
POST	/refine	Refine one section
🎥 Demo Checklist (for video)

Your video should cover:

✔ Login / Register
✔ Create DOCX project
✔ Add outline → Generate content
✔ Refine a section with AI prompt
✔ Export DOCX
✔ Create PPTX project
✔ Generate slides → Export PPTX
✔ Quick look at backend code + API docs

🧪 Testing

You can test all backend routes via Swagger UI:
👉 http://localhost:8000/docs

📦 Deployment (Optional)

Backend → Render / Railway / Fly.io

Frontend → Vercel / Netlify

DB → SQLite local or switch to PostgreSQL for production

🙌 Acknowledgements

Google Gemini API

FastAPI

React

python-docx & python-pptx

⭐ Conclusion

This project fulfills 100% of the assignment requirements, including:

Authentication

Document configuration

AI generation

Refinement UI

Export functionality

Clean codebase

Proper documentation
