from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.url import URL
from app.schemas.url import ShortenRequest, URLResponse
import random
import string

router = APIRouter()

def generate_short_code(db: Session):
    characters = string.ascii_letters + string.digits
    while True:
        short_code = ''.join(random.choices(characters, k=6))
        existing = db.query(URL).filter(URL.short_code == short_code).first()
        if not existing:
            return short_code

@router.post("/shorten", response_model=URLResponse)
def shorten_url(request: ShortenRequest, db: Session = Depends(get_db)):
    url_str = str(request.url)  # convert HttpUrl to plain string
    
    existing_url = db.query(URL).filter(URL.original_url == url_str).first()
    if existing_url:
        return existing_url
    
    short_code = generate_short_code(db)
    
    new_url = URL(
        original_url=url_str,
        short_code=short_code
    )
    
    db.add(new_url)
    db.commit()
    db.refresh(new_url)
    
    return new_url

@router.get("/links", response_model=list[URLResponse])
def get_links(limit: int = 10, offset: int = 0, db: Session = Depends(get_db)):
    urls = db.query(URL).order_by(URL.click_count.desc()).offset(offset).limit(limit).all()
    return urls

@router.get("/stats/{short_code}", response_model=URLResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return url

@router.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_code == short_code).first()
    
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    url.click_count += 1
    db.commit()
    
    return RedirectResponse(url=url.original_url)
