from pydantic import BaseModel, EmailStr
from typing import List

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    posts: List[str]
    subTopiqs: List[str]
    upVotes: List[str] 
    downVotes: List[str]
