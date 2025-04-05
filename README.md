# test-company-api
Arbetsprov API Exsitec 

# test-company-api
Arbetsprov API Exsitec 

API Ska göra: 

Produkt Katalog: Namn, kategori, beskrivning etc 
Prisinformation: Nuvarande pris, rabatter 
Lagersaldo 
Eventuellt: Authentication - limit access trusted resellers 

Planera för: 
Orderhantering 
Produktuppdateringar - för interna verktyg 


API Structure: 
Products: 
endpoint: /products - GET - list all products 
endpoint: /products{id} - GET - get specific product 

Inventory: 
endpoint: /inventory{product_id} - GET - get inventory for specific product 

Pricing:
endpoint: /pricing/{product_id} - GET - get pricing info for product 

Authentication:
endpoint: /auth/login - POST - login to get a token (JWT)


TEKNIK ATT ANVÄNDA: 
- Python 
- FastAPI 
- Pydantic - for data validation 
- Uvicorn - ASGI server to run the API 
- SQLite - DB to store data 


TO DO: 
Set up database SQLite 