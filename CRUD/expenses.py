from bson import ObjectId
from CRUD.settlements import insert_settlement

async def insert_expense(expense, db):
    expense_dict = expense.dict()
    expense_dict["_id"] = str(ObjectId())
    result = await db["Expenses"].insert_one(expense_dict)
    await insert_settlement(expense_dict, db)
    return expense_dict

async def get_expenses_by_group(group_id: str, db):
    return await db["Expenses"].find({"group_id": group_id}).to_list(length=100)
