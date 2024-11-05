from fastapi import APIRouter, HTTPException, Depends, status
from bson import ObjectId

from models.UserModel import *
from security import * 
from database import *


# Create router
user_router = APIRouter()

# Register endpoint
@user_router.post("/register", response_model=User)
async def register_user(user: UserCreate):
    hashed_password = get_password_hash(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    user_data["posts"] = []
    user_data["upVotes"] = []
    user_data["downVotes"] = []
    user_data["subTopiqs"] = []
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
# Logout endpoint (client should handle token invalidation)
@user_router.post("/logout")
async def logout():
    return {"message": "User logged out successfully"}

# List all users
@user_router.get("/all", response_model=List[User])
async def list_all_users():
    users = db.users.find()
    return [
        {
            "id": str(user["_id"]),
            "username": user["username"],
            "email": user["email"],
            "phone": user["phone"],
            "posts": user["posts"],
            "subTopiqs": user["subTopiqs"],
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
        "id": str(user["_id"]),
        "username": user["username"],
        "email": user["email"],
        "phone": user["phone"],
        "posts": user["posts"],
        "subTopiqs": user["subTopiqs"],
        "upVotes": user["upVotes"],
        "downVotes": user["downVotes"]
    }

# Delete a user by ID
@user_router.delete("/delete/{user_id}", response_model=dict)
async def delete_user(user_id: str):
    try:
        user_oid = ObjectId(user_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    # Check if the user exists
    user = db.users.find_one({"_id": user_oid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Delete the user from the users collection
    result = db.users.delete_one({"_id": user_oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="User not found")

    # Optionally, delete or update related records in other collections
    # For example, delete posts created by this user or remove subscriptions in subTopiqs
    db.posts.delete_many({"creatorId": user_oid})
    db.subTopiq.update_many({"moderators.moderatorId": user_oid}, {"$pull": {"moderators": {"moderatorId": user_oid}}})
    db.subTopiq.update_many({}, {"$pull": {"posts": {"postId": {"$in": user.get("posts", [])}}}})

    return {"message": f"User {user_id} and related data deleted successfully"}
