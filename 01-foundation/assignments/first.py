from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool

input_data = {'id':1,'name':'ghee','price':101,'in_stock':True}

product1= Product(input_data)

print(product1)
