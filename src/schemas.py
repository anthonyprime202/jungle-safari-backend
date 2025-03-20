from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    quantity: int
    price: float
    hsn_code: str = "40141010"  # Default HSN code for condoms

class OrderCreate(BaseModel):
    customer_name: str
    customer_email: str
    items: List[Item]

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class UserInDB(User):
    hashed_password: str

class UserCreate(BaseModel):
    username: str
    password: str
