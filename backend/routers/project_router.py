from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Project, Section
from schemas import ProjectCreate, ProjectOut
from utils.jwt_handler import decode_token
from services.ai_service import generate_section_content

router = APIRouter(prefix="/project", tags=["Project"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def auth(token: str = Header(...)):
    decoded = decode_token(token)
    if not decoded:
        raise HTTPException(401, "Invalid token")
    return decoded["user_id"]

@router.post("/create")
def create_project(data: ProjectCreate, user_id=Depends(auth), db: Session = Depends(get_db)):
    project = Project(
        user_id=user_id,
        title=data.title,
        doc_type=data.doc_type
    )
    db.add(project)
    db.commit()
    db.refresh(project)

    for section_title in data.outline:
        sec = Section(project_id=project.id, title=section_title, content="")
        db.add(sec)
    db.commit()

    return {"project_id": project.id}

@router.post("/{project_id}/generate", response_model=ProjectOut)
def generate_all(project_id: int, user_id=Depends(auth), db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
    if not project:
        raise HTTPException(404, "Project not found")

    for sec in project.sections:
        if not sec.content:
            sec.content = generate_section_content(sec.title)
    db.commit()

    return project

@router.get("/{project_id}", response_model=ProjectOut)
def get_project(project_id: int, user_id=Depends(auth), db: Session = Depends(get_db)):
    project = db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()
    if not project:
        raise HTTPException(404, "Project not found")

    return project
