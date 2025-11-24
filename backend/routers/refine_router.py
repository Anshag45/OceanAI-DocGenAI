from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Section
from schemas import SectionRefine
from utils.jwt_handler import decode_token
from services.ai_service import refine_content

router = APIRouter(prefix="/refine", tags=["Refine"])

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

@router.post("/")
def refine_section(data: SectionRefine, user_id=Depends(auth), db: Session = Depends(get_db)):
    section = db.query(Section).filter(Section.id == data.section_id).first()
    if not section:
        raise HTTPException(404, "Section not found")

    new = refine_content(section.content, data.prompt)
    section.content = new

    if data.comment:
        section.comment = data.comment

    db.commit()
    return {"updated": new}
