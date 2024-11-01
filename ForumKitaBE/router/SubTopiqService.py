from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from pymongo import MongoClient
from typing import List

from models.SubTopiqModel import *
from security import *
from database import *

# Create router
subtopiq_router = APIRouter()

# Create a subTopiq
@subtopiq_router.post("/create", response_model=SubTopiqBase)
async def create_subtopiq(name: str, creator_id: str):
    creator = db.users.find_one({"_id": ObjectId(creator_id)})
    if not creator:
        raise HTTPException(status_code=404, detail="Creator ID does not exist")

    # Check if a subTopiq with the same name already exists
    existing_subtopiq = db.subTopiq.find_one({"name": name})
    if existing_subtopiq:
        raise HTTPException(status_code=400, detail="SubTopiq name is already taken")

    # Proceed to create the subTopiq
    subtopiq_data = {
        "name": name,
        "creatorId": ObjectId(creator_id),
        "moderators": [],
        "posts": []
    }
    result = db.subTopiq.insert_one(subtopiq_data)
    subtopiq_data["id"] = str(result.inserted_id)
    subtopiq_data["creatorId"] = str(subtopiq_data["creatorId"])  # Convert ObjectId to string

    return subtopiq_data

# View all subTopiqs
@subtopiq_router.get("/all", response_model=List[SubTopiq])
async def view_all_subtopiqs():
    subtopiqs = db.subTopiq.find()
    return [
        {
            "id": str(sub["_id"]),
            "name": sub["name"],
            "creatorId": str(sub["creatorId"]),
            "moderators": [{"moderatorId": str(m["moderatorId"])} for m in sub.get("moderators", [])],
            "posts": [{"postId": str(p["postId"])} for p in sub.get("posts", [])]
        }
        for sub in subtopiqs
    ]

# View a subTopiq by ID
@subtopiq_router.get("/id/{subtopiq_id}", response_model=SubTopiq)
async def view_subtopiq_by_id(subtopiq_id: str):
    subtopiq = db.subTopiq.find_one({"_id": ObjectId(subtopiq_id)})
    if not subtopiq:
        raise HTTPException(status_code=404, detail="SubTopiq not found")
    return {
        "id": str(subtopiq["_id"]),
        "name": subtopiq["name"],
        "creatorId": str(subtopiq["creatorId"]),
        "moderators": [{"moderatorId": str(m["moderatorId"])} for m in subtopiq.get("moderators", [])],
        "posts": [{"postId": str(p["postId"])} for p in subtopiq.get("posts", [])]
    }

# View subTopiqs by moderator ID
@subtopiq_router.get("/moderated/{moderator_id}", response_model=List[SubTopiq])
async def view_subtopiq_by_moderator_id(moderator_id: str):
    moderator_oid = db.users.find_one({"_id": ObjectId(moderator_id)})['_id']
    if not moderator_oid:
        raise HTTPException(status_code=400, detail="Moderator not found")
    # Find subTopiqs where the given moderator ID exists in the moderators list
    subtopiqs = db.subTopiq.find({"moderators.moderatorId": moderator_oid})

    # Convert results to the desired format
    return [
        {
            "id": str(sub["_id"]),
            "name": sub["name"],
            "creatorId": str(sub["creatorId"]),
            "moderators": [{"moderatorId": str(m["moderatorId"])} for m in sub.get("moderators", [])],
            "posts": [{"postId": str(p["postId"])} for p in sub.get("posts", [])]
        }
        for sub in subtopiqs
    ]

# View subTopiqs by creator ID
@subtopiq_router.get("/created/{creator_id}", response_model=List[SubTopiq])
async def view_subtopiq_by_creator_id(creator_id: str):
    subtopiqs = db.subTopiq.find({"creatorId": ObjectId(creator_id)})
    if not subtopiqs:
        raise HTTPException(status_code=404, detail="SubTopiq not found")

    return [
        {
            "id": str(sub["_id"]),
            "name": sub["name"],
            "creatorId": str(sub["creatorId"]),
            "moderators": [{"moderatorId": str(m["moderatorId"])} for m in sub.get("moderators", [])],
            "posts": [{"postId": str(p["postId"])} for p in sub.get("posts", [])]
        }
        for sub in subtopiqs
    ]

# Add a moderator to a subTopiq
@subtopiq_router.post("/addmod/{subtopiq_id}/{user_id}")
async def add_moderator_to_subtopiq(subtopiq_id: str, user_id: str, current_user=Depends(get_current_user)):
    subtopiq = db.subTopiq.find_one({"_id": ObjectId(subtopiq_id)})
    if not subtopiq:
        raise HTTPException(status_code=404, detail="SubTopiq not found")

    user = db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if any(mod["moderatorId"] == ObjectId(user_id) for mod in subtopiq.get("moderators", [])):
        raise HTTPException(status_code=400, detail="User is already a moderator")

    db.subTopiq.update_one(
        {"_id": ObjectId(subtopiq_id)},
        {"$push": {"moderators": {"moderatorId": ObjectId(user_id)}}}
    )

    return {"message": f"User {user_id} added as a moderator to SubTopiq {subtopiq_id}"}


