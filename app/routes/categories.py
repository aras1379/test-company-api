from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app import models, schemas 

router = APIRouter(
    prefix = "/categories",
    tags = ["Categories"]
)


@router.get("/", response_model=list[schemas.CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()

@router.post("/", response_model=schemas.CategoryOut)
def create_category(category: schemas.CategoryCreate, db: Session=Depends(get_db)):
    category_name = category.name.lower().strip()
    exists = db.query(models.Category).filter_by(name=category_name).first()
    if exists:
        raise HTTPException(status_code=400, detail="category exists")
    db_category = models.Category(name = category_name) 
    #**category.dict() same as name = category.name
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category