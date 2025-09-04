# Goa Trip Expense Manager

## Overview
This project is a backend API for managing group expenses, settlements, and user authentication for a Goa trip. It uses FastAPI, MongoDB, and JWT authentication.

---

## Project Workflow

### 1. **User Registration & Authentication**
- Users register with name, email, age, and password.
- Passwords are securely hashed.
- JWT tokens are issued upon login for secure API access.

### 2. **Group Management**
- Users can create groups for the trip.
- Each group has a name, description, and a list of members (user IDs).
- Groups are stored in MongoDB with `ObjectId` as the unique identifier.

### 3. **Expense Tracking**
- Expenses can be added to groups.
- Each expense records the group, description, amount, payer, and members sharing the expense.
- Data is stored in the `Expenses` collection.

### 4. **Settlement Calculation**
- Settlements track who owes whom and how much within a group.
- Each settlement records the group, sender, receiver, and amount.

### 5. **Authentication Workflow**
- JWT tokens are used for all protected routes.
- Token is decoded to get user info (using MongoDB `ObjectId`).
- All group and expense actions are tied to the authenticated user.

---

## Data Models

### User
```python
class User(BaseModel):
    name: str
    email: str
    age: int
    password: str
```

### Groups
```python
class Groups(BaseModel):
    name: str
    description: Optional[str] = None
    members: list[str]  # List of user ObjectIds
```

### Expenses
```python
class Expenses(BaseModel):
    group_id: str  # MongoDB ObjectId
    description: str
    amount: float
    paid_by: str  # User ObjectId
    split_between: list[str]  # User ObjectIds
```

### Settlements
```python
class Settlements(BaseModel):
    group_id: str
    from_user: str
    to_user: str
    amount: float
```

---

## API Endpoints

- **POST /register**: Register a new user
- **POST /login**: Authenticate and get JWT token
- **POST /create_group**: Create a new group
- **GET /get_groups_based_on_user/{id}**: Get groups for a user
- **POST /add_expense**: Add an expense to a group
- **GET /get_expenses/{group_id}**: Get expenses for a group
- **POST /settle**: Record a settlement

---

## Technologies Used
- FastAPI
- MongoDB
- Pydantic
- JWT (JSON Web Tokens)
- Python

---

## Example Workflow
1. Register/Login to get JWT token.
2. Create a group and add members.
3. Add expenses to the group.
4. View group expenses and settlements.
5. Settle up balances between users.

---

## Author
Made with ❤️ fork.
