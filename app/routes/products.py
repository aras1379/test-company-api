from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app import models, schemas 

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/", response_model=list[schemas.ProductOut])
def get_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@router.post("/", response_model=schemas.ProductOut)
def create_product(product: schemas.ProductCreate, db: Session=Depends(get_db)):
    existing = db.query(models.Product).filter_by(name=product.name).first() 
    if existing:
        raise HTTPException(status_code=400, detail="product with that name exists already")
    category = db.query(models.Category).filter_by(name=product.category).first()
    if not category:
        raise HTTPException(status_code=400, detail="category not found")
    
    db_product = models.Product(
        name=product.name,
        category_id=category.id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product