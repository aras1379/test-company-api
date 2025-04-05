from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session 
from app.database import get_db
from app import models, schemas 

router = APIRouter(
    prefix="/currency",
    tags=["Currency"]
)

@router.get("/", response_model=list[schemas.CurrencyOut])
def get_all_currencies(db: Session = Depends(get_db)):
    return db.query(models.Currency).all() 

@router.post("/", response_model=schemas.CurrencyOut)
def create_currency(currency: schemas.CurrencyCreate, db: Session=Depends(get_db)):
    db_currency = models.Currency(**currency.dict())
    db.add(db_currency)
    db.commit()
    db.refresh(db_currency)
    return db_currency 
