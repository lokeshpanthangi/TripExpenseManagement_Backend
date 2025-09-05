from fastapi import Depends, HTTPException, APIRouter
from auth import validate
from database import db
from CRUD.groups import delete_group_member, insert_group, get_groups_by_user, add_member_to_group, get_group_by_id
from pydantic_schemas import Groups

group_router = APIRouter()


@group_router.post("/create_group")
async def create_group_route(group: Groups, tokendata: dict = Depends(validate)):
    new_group = await insert_group(group, tokendata, db)
    return {"group": new_group}


@group_router.get("/get_groups_based_on_user/{id}")
async def get_groups_based_on_user_route(id: str, dict = Depends(validate)):
    groups = await get_groups_by_user(id, db)
    return {"groups": groups}


@group_router.get("/group_data/{group_id}")
async def get_group_data_route(group_id: str,dict = Depends(validate)):
    group = await get_group_by_id(group_id, db)
    if group:
        return {"group": group}
    raise HTTPException(status_code=404, detail="Group not found")


@group_router.get("/add_member/{group_id}/add_member/{user_id}")
async def add_member_to_group_route(group_id: str, user_id: str, dict = Depends(validate)):
    result = await add_member_to_group(group_id, user_id, db)
    if result is True:
        return {"message": "Member added successfully"}
    elif result is False:
        return {"message": "Member already in group"}
    return {"message": "Group not found"}


@group_router.post("/delete_user/{user_id}/from/{group_id}")
async def delete_user_route(user_id: str, group_id: str, dict = Depends(validate)):
    result = await delete_group_member(group_id, user_id, db)
    if result:
        return {"detail": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
