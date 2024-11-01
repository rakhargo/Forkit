from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import datetime, timedelta

# Models
class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: str
    upVotes: int = 0
    downVotes: int = 0

class SubTopiqBase(BaseModel):
    name: str
    creator: str
    moderator: str

class SubTopiq(SubTopiqBase):
    id: str
    posts: List[str] = []

class PostBase(BaseModel):
    title: str
    description: str
    creator: str
    sub_topiq_id: str

class Post(PostBase):
    id: str
    upVotes: int = 0
    downVotes: int = 0
    replies: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Reply(BaseModel):
    post_id: str
    content: str
    creator: str
    created_at: datetime = Field(default_factory=datetime.utcnow)


