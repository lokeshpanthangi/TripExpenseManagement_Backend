from auth import decode_token
from fastapi import HTTPException, APIRouter
from database import db
from CRUD.groups import insert_group, get_groups_by_user, add_member_to_group, get_group_by_id
from pydantic_schemas import Groups


group_router = APIRouter()

@group_router.post("/create_group")
async def create_group_route(group: Groups , token: str):
    tokendata = decode_token(token)
    if tokendata == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    new_group = await insert_group(group, tokendata, db)
    return {"group": new_group}

@group_router.get("/get_groups_based_on_user/{id}")
async def get_groups_based_on_user_route(id: str, token: str):
    if decode_token(token) == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    groups = await get_groups_by_user(id, db)
    return {"groups": groups}


@group_router.get("/group_data/{group_id}")
async def get_group_data_route(group_id: str, token: str):
    if decode_token(token) == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    group = await get_group_by_id(group_id, db)
    if group:
        return {"group": group}
    raise HTTPException(status_code=404, detail="Group not found")


@group_router.get("/add_member/{group_id}/add_member/{user_id}")
async def add_member_to_group_route(group_id: str, user_id: str, token: str):
    if decode_token(token) == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    result = await add_member_to_group(group_id, user_id, db)
    if result is True:
        return {"message": "Member added successfully"}
    elif result is False:
        return {"message": "Member already in group"}
    return {"message": "Group not found"}
