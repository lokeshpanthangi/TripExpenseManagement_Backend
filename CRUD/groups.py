from bson import ObjectId


async def insert_group(group, tokendata, db):
    group_dict = group.dict()
    group_dict["_id"] = str(ObjectId())
    group_dict["created_by"] = tokendata["_id"]
    result = await db["Groups"].insert_one(group_dict)
    new_group = await db["Groups"].find_one({"_id": group_dict["_id"]})
    return new_group


#members is a list of user ids who are part of the group
async def get_groups_by_user(id: str, db):
    return await db["Groups"].find({"members": id}).to_list(length=100)