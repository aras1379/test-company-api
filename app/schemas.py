from pydantic import BaseModel, computed_field

#models 
class CategoryOut(BaseModel):
    id: int 
    name: str 
    
    class Config: 
        from_attributes = True 

class CategoryCreate(BaseModel):
    name: str

class ProductOut(BaseModel):
    id: int 
    name: str 
    category: CategoryOut 
    
    class Config: 
        from_attributes = True 
        
class ProductCreate(BaseModel):
    name: str
    category: str 

class InventoryCreate(BaseModel):
    product_name: str
    stock: int 
    
class InventoryOut(BaseModel):
    id: int
    stock: int
    product: ProductOut 
    
    class Config:
        from_attributes = True 
        
        

    

class CurrencyOut(BaseModel):
    id: int 
    name: str
    
    class Config:
        from_attributes = True 

class CurrencyCreate(BaseModel):
    name: str 

class PricingCreate(BaseModel):
    product_name: str 
    price: float 
    currency: str 
    
class PricingOut(BaseModel):
    id: int
    product: ProductOut 
    price: float
    currency: CurrencyOut 
    
    @computed_field
    def priceWMoms(self) -> float: 
        return round(self.price * 1.2, 2) #20% tax
    
    class Config:
        from_attributes = True 