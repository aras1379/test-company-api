from fastapi import FastAPI, Depends 
from pydantic import BaseModel
from sqlalchemy.orm import Session 
from app.database import engine 
from app.routes import products, categories, currency, inventory, pricing 
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI() 

app.include_router(products.router, tags=["Products"])
app.include_router(categories.router, tags=["Categories"])
app.include_router(currency.router, tags=["Currency"])
app.include_router(inventory.router, tags=["Inventory"])
app.include_router(pricing.router, tags=["Pricing"])



@app.get("/")
def read_root():
    return {"message": "Welcomde to EskiTech API"}
