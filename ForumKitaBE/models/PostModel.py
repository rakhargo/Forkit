from pydantic import BaseModel
from typing import List

class Reply(BaseModel):
    reply: str
    creatorId: str

class Post(BaseModel):
    id: str
    title: str
    description: str
    upVote: int = 0
    downVote: int = 0
    replies: List[Reply] = []
    creatorId: str
    subTopiqId: str

