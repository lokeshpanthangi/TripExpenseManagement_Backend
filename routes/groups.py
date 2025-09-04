from auth import decode_token
from fastapi import HTTPException, APIRouter
from database import db
from CRUD.groups import insert_group, get_groups_by_user
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
    groups = await get_groups_by_user(id, db)
    return {"groups": groups}

@group_router.get("/test_decode")
async def test_decode_route(token : str):
    tokendata = decode_token(token)
    if tokendata == "Invalid token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"token_data": tokendata}