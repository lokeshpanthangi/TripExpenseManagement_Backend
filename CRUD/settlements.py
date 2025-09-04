from bson import ObjectId


async def insert_settlement(expense_dict, db):
    members_count = len(expense_dict["split_between"]) + 1
    split_amount = expense_dict["amount"] / members_count
    d = {}
    for member in expense_dict["split_between"]:
        d[member] = split_amount
    d[expense_dict["paid_by"]] = split_amount - expense_dict["amount"]
    results = await db["Settlements"].insert_one({
        "_id": str(ObjectId()),
        "expense_id": expense_dict["_id"],
        "settlements": d,
        "group_id": expense_dict["group_id"]
    })

async def paid_user_to_user(expense_id: str, settlements: dict, db):
    result = await db["Settlements"].find_one({"expense_id": expense_id})
    a = settlements["from_user"]
    b = settlements["to_user"]
    amount = settlements["amount"]
    if result:
        current_settlements = result["settlements"]
        current_settlements[a] += amount
        current_settlements[b] -= amount
        await db["Settlements"].update_one(
            {"expense_id": expense_id},
            {"$set": {"settlements": current_settlements}}
        )
        return current_settlements