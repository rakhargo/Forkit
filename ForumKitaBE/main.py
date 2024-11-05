from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Optional
from jose import JWTError, jwt
import uvicorn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

from router import *

# MongoDB connection
MONGO_URL = "mongodb://localhost:27017"
client = MongoClient(MONGO_URL)
db = client.forumKitaDb

# Initialize FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include routers from each service module
app.include_router(user_router, prefix="/user", tags=["User"])
app.include_router(subtopiq_router, prefix="/subtopiq", tags=["SubTopiq"])
app.include_router(post_router, prefix="/posts", tags=["Post"])

