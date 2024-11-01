from fastapi import APIRouter, HTTPException, Depends, status
from bson import ObjectId

from models.UserModel import *
from security import * 
from database import *


# Create router
user_router = APIRouter()

# Utility function to convert ObjectId to string
def str_objectid(oid):
    return str(oid) if isinstance(oid, ObjectId) else oid

@user_router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    user_data["posts"] = []
    user_data["upVotes"] = []
    user_data["downVotes"] = []
    result = db.users.insert_one(user_data)
    user_data["id"] = str(result.inserted_id)
    return user_data

@user_router.post("/token")
async def token_login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.users.find_one({"username": form_data.username})
    if not user or not verify_password(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user["username"]})
    return {"access_token": access_token, "token_type": "bearer"}

# User-friendly login endpoint
@user_router.post("/login")
async def login(username: str, password: str):
    user = db.users.find_one({"username": username})
    if not user or not verify_password(password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    user_id = str(user["_id"])
    access_token = create_access_token(data={"sub": user["username"]})
    return {
        "access_token": access_token,
        "token_type": "bearer",
        "user_id": user_id  # Include user ID in the response
    }

# List all users
@user_router.get("/all", response_model=List[User])
async def list_all_users():
    users = db.users.find()
    return [
        {
            "id": str_objectid(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "phone": user["phone"],
            "posts": user["posts"],
            "upVotes": user["upVotes"],
            "downVotes": user["downVotes"]
        }
        for user in users
    ]

# Get user by ID
@user_router.get("/id/{user_id}", response_model=User)
async def get_user_by_id(user_id: str):
    try:
        user_oid = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")
    
    user = db.users.find_one({"_id": user_oid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    return {
        "id": str_objectid(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "phone": user["phone"],
        "posts": user["posts"],
        "upVotes": user["upVotes"],
        "downVotes": user["downVotes"]
    }

# Logout endpoint (client should handle token invalidation)
@user_router.post("/logout")
async def logout():
    return {"message": "User logged out successfully"}
