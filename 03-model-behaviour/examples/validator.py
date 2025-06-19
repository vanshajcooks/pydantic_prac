# learneing about  model validator and field validator
from pydantic import BaseModel,field_validator,model_validator,computed_field #type: ignore


class User(BaseModel):
    username: str  # wanna write customised validations

    @field_validator('username')
    def username_length(cls,v):   #cls for class and v for value yeh humari do fields
        if len(v)<4:
            raise ValueError("Username must be atleast 4 characters")
        return v
    

class SignupData(BaseModel):
    password:str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls,values):
        if values.password != values.confirm_password:
            raise ValueError("password donot match")
        return values
    
class Product(BaseModel):
    price: float
    quantity: int


    @computed_field
    @property # khud ki hi apni ek property banadega which we can use later
    def total_price(self)-> float:
        return self.price * self.quantity