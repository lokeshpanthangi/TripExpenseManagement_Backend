import uuid



async def insert_group(group, db):
    group_dict = group.dict()
    group_dict["_id"] = str(uuid.uuid4())
    result = await db["Groups"].insert_one(group_dict)
    new_group = await db["Groups"].find_one({"_id": group_dict["_id"]})
    return new_group