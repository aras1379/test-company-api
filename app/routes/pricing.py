from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload 
from app.database import get_db
from app import models, schemas 

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)

@router.get("/{product_id}", response_model=schemas.PricingOut)
def get_price(product_id: int, db: Session = Depends(get_db)):
    price = (
        db.query(models.Pricing)
        .options(joinedload(models.Pricing.product), joinedload(models.Pricing.currency))  # 🔥 Ensure joins!
        .filter_by(product_id=product_id)
        .first()
    )
    if not price:
        raise HTTPException(status_code=404, detail="Pricing not found")
    return price

@router.post("/", response_model=schemas.PricingOut)
def set_price(data: schemas.PricingCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter_by(name=data.product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    
    currency = db.query(models.Currency).filter_by(name=data.currency).first()
    if not currency:
        raise HTTPException(status_code=404, detail="currency not found")
    
    new_price = models.Pricing(
        product_id=product.id, 
        price=data.price,
        currency=currency
        
    )
    db.add(new_price)
    db.commit()
    db.refresh(new_price)
    return new_price

@router.put("/{product_id}", response_model=schemas.PricingOut)
def update_price(product_id: int, price_data: schemas.PricingCreate, db: Session = Depends(get_db)):
    price = db.query(models.Pricing).filter_by(product_id=product_id).first()
    if not price:
        raise HTTPException(status_code=404, detail="Pricing not found")

    currency = db.query(models.Currency).filter_by(name=price_data.currency).first()
    if not currency:
        raise HTTPException(status_code=404, detail="Currency not found")

    price.price = price_data.price
    price.currency = currency 

    db.commit()
    db.refresh(price)
    return price
