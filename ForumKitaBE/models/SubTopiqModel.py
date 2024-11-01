from pydantic import BaseModel
from typing import List

class Moderator(BaseModel):
    moderatorId: str

class PostReference(BaseModel):
    postId: str

class SubTopiqBase(BaseModel):
    name: str
    creatorId: str
    moderators: List[Moderator] = []
    posts: List[PostReference] = []

class SubTopiq(SubTopiqBase):
    id: str
  
