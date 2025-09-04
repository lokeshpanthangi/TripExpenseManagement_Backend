from bson import ObjectId


async def insert_expense(expense, db):
    expense_dict = expense.dict()
    expense_dict["_id"] = str(ObjectId())
    result = await db["Expenses"].insert_one(expense_dict)
    new_expense = await db["Expenses"].find_one({"_id": expense_dict["_id"]})
    return new_expense


async def get_expenses_by_group(group_id: str, db):
    return await db["Expenses"].find({"group_id": group_id}).to_list(length=100)

