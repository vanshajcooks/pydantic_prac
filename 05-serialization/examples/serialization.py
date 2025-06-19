from pydantic import BaseModel,ConfigDict #type:ignore
from typing import List
from datetime import datetime

#Dump and Dumpjson

class Address(BaseModel):
    street: str
    city:str
    pincode: str


class User(BaseModel):
    id: int
    name:str
    email: str
    isActive: bool = True
    createdAt: datetime
    address: Address
    tags:List[str] = []


    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    ) # agar meko json format mein datetime ka modification karna mere according ya koi similar conifgurations toh ConfigDict use karo from pydantic

#create a user instance


user = User(
    id= 1,
    name="vasnsh",
    email= "ags@hc.com",
    isActive=True,
    createdAt= datetime(2024,3,15,14,30),
    address= Address(
        street = "somehti",
        city = "hsp",
        pincode ="123"
    ),
    tags=["prem","sub"]
)



# Using model_dump() ---> dict (expected ouptut)


python_dict= user.model_dump()

print(python_dict)

#using modelu_dump_json() ---> json milega
print("======================================\n")

json_str = user.model_dump_json()

print(json_str)


