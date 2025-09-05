from bson import ObjectId


async def insert_group(group, tokendata, db):
    group_dict = group.dict()
    group_dict["_id"] = str(ObjectId())
    group_dict["created_by"] = tokendata["_id"]

    # Build members dict in one go
    members = {member: "member" for member in group_dict["members"]}
    members[group_dict["created_by"]] = "Admin"
    group_dict["members"] = members

    await db["Groups"].insert_one(group_dict)
    return group_dict  # no need to fetch again, we already have it


async def get_groups_by_user(user_id: str, db):
    cursor = db["Groups"].find({f"members.{user_id}": {"$exists": True}})
    result = await cursor.to_list(length=100)
    return result



async def add_member_to_group(group_id: str, user_id: str, db):
    group = await db["Groups"].find_one({"_id": group_id})
    if group:
        if user_id not in group["members"]:
            await db["Groups"].update_one({"_id": group_id}, {"$set": {f"members.{user_id}": "member"}})
            return True
        return False
    return None


async def get_group_by_id(group_id: str, db):
    return await db["Groups"].find_one({"_id": group_id})

async def delete_group_member(group_id: str, user_id: str, db):
    group = await db["Groups"].find_one({"_id": group_id})
    if group:
        if user_id in group["members"]:
            await db["Groups"].update_one({"_id": group_id}, {"$unset": {f"members.{user_id}": ""}})
            return True
        return False
    
