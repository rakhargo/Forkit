from pydantic import BaseModel, EmailStr
from typing import List

class PostReference(BaseModel):
    postId: str

class SubTopiqReference(BaseModel):
    subTopiqId: str

class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    posts: List[PostReference] = []
    upVotes: List[PostReference] = []
    downVotes: List[PostReference] = []
    subTopiqs: List[SubTopiqReference] = []

class LoginRequest(BaseModel):
    username: str
    password: str
