from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session 
from app.database import get_db
from app import models, schemas 

router = APIRouter(
    prefix = "/inventory",
    tags = ["Inventory"]
)

#get inventory
@router.get("/", response_model=list[schemas.InventoryOut])
def get_all_inventory(db: Session = Depends(get_db)):
    return db.query(models.Inventory).all()

@router.get("/{product_id}", response_model=schemas.InventoryOut)
def get_inventory(product_id: int, db: Session=Depends(get_db)):
    inv = db.query(models.Inventory).filter_by(product_id=product_id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inv 

@router.get("/by-product-name/{name}", response_model=schemas.InventoryOut)
def get_inventory_by_name(name: str, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter_by(name=name).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    inv = db.query(models.Inventory).filter_by(product_id=product.id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="Inventory not found")
    return inv

@router.post("/", response_model=schemas.InventoryOut)
def set_inventory(inv_data: schemas.InventoryCreate, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter_by(name=inv_data.product_name).first()
    if not product:
        raise HTTPException(status_code=404, detail="product not found")
    db_inventory = models.Inventory(product_id=product.id, stock=inv_data.stock)
    db.add(db_inventory)
    db.commit()
    db.refresh(db_inventory)
    return db_inventory

@router.put("/{product_id}", response_model=schemas.InventoryOut)
def update_inventory(product_id: int, inv_data: schemas.InventoryCreate, db: Session = Depends(get_db)):
    inv = db.query(models.Inventory).filter_by(product_id=product_id).first()
    if not inv:
        raise HTTPException(status_code=404, detail="inventory not found")
    inv.stock = inv_data.stock 
    db.commit()
    db.refresh(inv)
    return inv 
## SHOULD HAVE POST FUNC?? 