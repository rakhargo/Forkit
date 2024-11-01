from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional
from jose import JWTError, jwt
import uvicorn

from schemas import *
from services import *

# MongoDB connection
MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client.forumKitaDb
app = FastAPI()

# Register endpoint
@app.post("/register/", response_model=User)
async def create_user(user: UserCreate):
    if db.users.find_one({"username": user.username}):
        raise HTTPException(status_code=400, detail="Username already registered")
    
    hashed_password = get_password_hash(user.password)
    user_dict = user.dict()
    user_dict["password"] = hashed_password
    user_dict["upVote"] = []
    user_dict["downVote"] = []
    
    result = db.users.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

# Create subtopiqs
@app.post("/subtopiqs/", response_model=SubTopiq)
async def create_subtopiq(subtopiq: SubTopiqBase, current_user: dict = Depends(get_current_user)):
    subtopiq_dict = subtopiq.dict()
    subtopiq_dict["posts"] = []
    result = db.subTopiq.insert_one(subtopiq_dict)
    subtopiq_dict["id"] = str(result.inserted_id)
    return subtopiq_dict

# Create posts
@app.post("/posts/", response_model=Post)
async def create_post(post: PostBase, current_user: dict = Depends(get_current_user)):
    post_dict = post.dict()
    post_dict["upVote"] = 0
    post_dict["downVote"] = 0
    post_dict["replies"] = []
    post_dict["created_at"] = datetime.utcnow()
    
    result = db.posts.insert_one(post_dict)
    post_dict["id"] = str(result.inserted_id)
    
    # Update subtopiq's posts list
    db.subTopiq.update_one(
        {"_id": ObjectId(post.sub_topiq_id)},
        {"$push": {"posts": str(result.inserted_id)}}
    )
    
    return post_dict

# Upvote a post
@app.post("/posts/{post_id}/vote")
async def vote_post(post_id: str, vote_type: str, current_user: dict = Depends(get_current_user)):
    if vote_type not in ["up", "down"]:
        raise HTTPException(status_code=400, detail="Invalid vote type")
    
    update_field = "upVote" if vote_type == "up" else "downVote"
    result = db.posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$inc": {update_field: 1}}
    )
    
    if result.modified_count == 0:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return {"message": f"{vote_type.capitalize()}vote recorded"}

# Reply to a post
@app.post("/posts/{post_id}/reply")
async def add_reply(post_id: str, reply: Reply, current_user: dict = Depends(get_current_user)):
    reply_dict = reply.dict()
    reply_dict["created_at"] = datetime.utcnow()
    
    result = db.replies.insert_one(reply_dict)
    reply_id = str(result.inserted_id)
    
    db.posts.update_one(
        {"_id": ObjectId(post_id)},
        {"$push": {"replies": reply_id}}
    )
    
    return {"message": "Reply added successfully", "reply_id": reply_id}

# Get a specific post
@app.get("/posts/{post_id}", response_model=Post)
async def get_post(post_id: str):
    post = db.posts.find_one({"_id": ObjectId(post_id)})
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post["id"] = str(post["_id"])
    return post

# Get a specific subtopiq
@app.get("/subtopiqs/{subtopiq_id}/posts", response_model=List[Post])
async def get_subtopiq_posts(subtopiq_id: str):
    posts = list(db.posts.find({"sub_topiq_id": subtopiq_id}))
    for post in posts:
        post["id"] = str(post["_id"])
    return posts

@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.users.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

