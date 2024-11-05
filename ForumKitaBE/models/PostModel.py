from pydantic import BaseModel
from typing import List, Optional

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

class PostWithUser(BaseModel):
    id: str
    title: str
    description: str
    upVote: int
    downVote: int
    creatorId: str
    creatorUsername: str  # Field for joined user data
    creatorEmail: str     # Field for joined user data
    replies: Optional[List[str]] = []
