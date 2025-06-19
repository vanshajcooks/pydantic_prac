from pydantic import BaseModel #type:ignore
from typing import List,Optional

# NESTED MODELS - Ek model jo ek aur model ko refer karre ho

class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name:str
    address: Address  # nested model referencing yaha pe hori hai (upar wali class ko refer karra hai yaha datatype)

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # self referencing hori hai yaha pe but this is not nice - forward referencing isko rebuild karwana hi padega MUST HAI (documentations mein likha to avoid errors karlena)

Comment.model_rebuild()


address = Address(
    street= "123something",
    city= "hsp",
    postal_code="102y7"
)

user = User(
    id= 1,
    name= "vansha",
    address= address
)


comment = Comment(
    id=2,
    content="first comment",
    replies=[Comment(id=3,content="reply1"),
             Comment(id=4,content="reply2")]
)