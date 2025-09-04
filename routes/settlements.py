from fastapi import APIRouter
from CRUD.settlements import paid_user_to_user
from database import db
from pydantic_schemas import Settlements
settlements_router = APIRouter()


@settlements_router.post("/settlements/{expense_id}")
async def settle_amount(expense_id: str, settlements: Settlements):
    result = await paid_user_to_user(expense_id, settlements.dict(), db)
    if result:
        return {"message": "Settlement updated successfully", "settlements": result}
    return {"message": "Expense not found"}