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

    existing_subtopiq = db.subTopiq.find_one({"name": name})
    if existing_subtopiq:
        raise HTTPException(status_code=400, detail="SubTopiq name is already taken")

    subtopiq_data = {
        "name": name,
        "creatorId": ObjectId(creator_id),
        "moderators": [{"moderatorId": ObjectId(creator_id)}], 
        "posts": []
    }

    result = db.subTopiq.insert_one(subtopiq_data)
    subtopiq_data["id"] = str(result.inserted_id)
    subtopiq_data["creatorId"] = str(subtopiq_data["creatorId"])  # Convert ObjectId to string
    subtopiq_data["moderators"] = [{"moderatorId": str(ObjectId(creator_id))}]  # Convert moderatorId to string

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
    subtopiqs = db.subTopiq.find({"moderators.moderatorId": moderator_oid})

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
# Subscribe to a subTopiq
@subtopiq_router.post("/subscribe/{user_id}/{subtopiq_id}")
async def subscribe_to_subtopiq(user_id: str, subtopiq_id: str):
    try:
        user_oid = ObjectId(user_id)
        subtopiq_oid = ObjectId(subtopiq_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user or subTopiq ID format")

    user = db.users.find_one({"_id": user_oid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the user is already subscribed to the subTopiq
    if any(str(sub["subTopiqId"]) == subtopiq_id for sub in user.get("subTopiqs", [])):
        raise HTTPException(status_code=400, detail="User is already subscribed to this subTopiq")

    # Push the subTopiq as a dictionary with "subTopiqId" key
    db.users.update_one({"_id": user_oid}, {"$push": {"subTopiqs": {"subTopiqId": str(subtopiq_oid)}}})
    
    return {"message": f"User {user_id} subscribed to SubTopiq {subtopiq_id}"}

# Unsubscribe from a subTopiq
@subtopiq_router.post("/unsubscribe/{user_id}/{subtopiq_id}")
async def unsubscribe_from_subtopiq(user_id: str, subtopiq_id: str):
    try:
        user_oid = ObjectId(user_id)
        subtopiq_oid = ObjectId(subtopiq_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid user or subTopiq ID format")

    user = db.users.find_one({"_id": user_oid})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check if the user is subscribed to the subTopiq
    if not any(str(sub["subTopiqId"]) == subtopiq_id for sub in user.get("subTopiqs", [])):
        raise HTTPException(status_code=400, detail="User is not subscribed to this subTopiq")

    # Pull the subTopiq from subTopiqs based on subTopiqId
    db.users.update_one({"_id": user_oid}, {"$pull": {"subTopiqs": {"subTopiqId": str(subtopiq_oid)}}})
    
    return {"message": f"User {user_id} unsubscribed from SubTopiq {subtopiq_id}"}

# Delete a subTopiq by ID
@subtopiq_router.delete("/delete/{subtopiq_id}", response_model=dict)
async def delete_subtopiq(subtopiq_id: str):
    try:
        subtopiq_oid = ObjectId(subtopiq_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid subTopiq ID format")

    subtopiq = db.subTopiq.find_one({"_id": subtopiq_oid})
    if not subtopiq:
        raise HTTPException(status_code=404, detail="SubTopiq not found")

    result = db.subTopiq.delete_one({"_id": subtopiq_oid})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="SubTopiq not found")


    db.posts.delete_many({"subTopiqId": subtopiq_oid})
    db.users.update_many({}, {"$pull": {"subTopiqs": subtopiq_id}})
    return {"message": f"SubTopiq {subtopiq_id} and related data deleted successfully"}

# Fetch subTopiq with mod details TUH UDH JOIN YAAAAAAA GW MW TURU
@subtopiq_router.get("/subtopiqs-all/{subtopiq_id}")
async def get_subtopiq_with_moderators_and_posts(subtopiq_id: str):
    try:
        subtopiq_oid = ObjectId(subtopiq_id)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid subTopiq ID format")

    subtopiq_with_moderators_and_posts = db.subTopiq.aggregate([
        {"$match": {"_id": subtopiq_oid}},  # Match specific subTopiq by ID
        {
            "$lookup": {
                "from": "users",
                "localField": "creatorId",
                "foreignField": "_id",
                "as": "creator"
            }
        },
        {"$unwind": "$creator"},  # Flatten the creator array
        {
            "$lookup": {
                "from": "users",  # Join with users to get moderator details
                "localField": "moderators.moderatorId",
                "foreignField": "_id",
                "as": "moderators_info"
            }
        },
        {
            "$lookup": {
                "from": "posts",  # Join with posts collection to fetch posts for the subTopiq
                "localField": "_id",
                "foreignField": "subTopiqId",
                "as": "posts_info"
            }
        }
    ])

    # Format result for JSON response
    result = next(subtopiq_with_moderators_and_posts, None)  # Get the first document if exists
    if not result:
        raise HTTPException(status_code=404, detail="SubTopiq not found")

    formatted_result = {
        "id": str(result["_id"]),
        "name": result["name"],
        "creator": {
            "id": str(result["creator"]["_id"]),
            "username": result["creator"]["username"],
            "email": result["creator"]["email"],
            "phone": result["creator"]["phone"]
        },
        "moderators": [
            {
                "id": str(mod["_id"]),
                "username": mod["username"],
                "email": mod["email"],
                "phone": mod["phone"]
            }
            for mod in result.get("moderators_info", [])
        ],
        "posts": [
            {
                "id": str(post["_id"]),
                "title": post["title"],
                "description": post["description"],
                "upVote": post["upVote"],
                "downVote": post["downVote"],
                "creatorId": str(post["creatorId"]),
                "replies": [
                    {"reply": r["reply"], "creatorId": str(r["creatorId"])}
                    for r in post.get("replies", [])
                ]
            }
            for post in result.get("posts_info", [])
        ]
    }

    return formatted_result

