from fastapi import APIRouter, Depends
from auth import validate
from database import db
from CRUD.expenses import insert_expense, get_expenses_by_group
from pydantic_schemas import Expenses


expense_router = APIRouter()

@expense_router.post("/add_expense")
async def add_expense_route(expense: Expenses, dict = Depends(validate)):
    new_expense = await insert_expense(expense, db)
    return {"expense": new_expense}


@expense_router.get("/get_expenses_by_group/{group_id}")
async def get_expenses_by_group_route(group_id: str, dict = Depends(validate)):
    expenses = await get_expenses_by_group(group_id, db)
    return {"expenses": expenses}