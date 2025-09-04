from fastapi import APIRouter
from auth import decode_token
from database import db
from CRUD.expenses import insert_expense, get_expenses_by_group
from pydantic_schemas import Expenses


expense_router = APIRouter()

@expense_router.post("/add_expense")
async def add_expense_route(expense: Expenses, token: str):
    if decode_token(token) == "Invalid token":
        return {"error": "Invalid token"}
    new_expense = await insert_expense(expense, db)
    return {"expense": new_expense}


@expense_router.get("/get_expenses_by_group/{group_id}")
async def get_expenses_by_group_route(group_id: str, token: str):
    if decode_token(token) == "Invalid token":
        return {"error": "Invalid token"}
    expenses = await get_expenses_by_group(group_id, db)
    return {"expenses": expenses}