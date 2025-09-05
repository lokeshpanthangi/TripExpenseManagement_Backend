from database import db

db = db  # Import the database instance from database.py


async def create_indexes(db):
    await db.Groups.create_index("members")
    await db.Expenses.create_index("group_id")
    await db.Settlements.create_index("group_id")

# Call the function to create indexes when the module is imported
import asyncio
asyncio.run(create_indexes(db))
print("Indexes created.")
