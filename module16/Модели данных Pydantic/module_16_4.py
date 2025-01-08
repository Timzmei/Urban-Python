from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel

app = FastAPI()

users = []

class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/users")
def read_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: str = Path(..., title="Enter username", min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
    age: int = Path(..., title="Enter age", ge=18, le=120, description="Enter age", example=24)
):
    new_user_id = len(users) + 1 if users else 1
    new_user = User(id=new_user_id, username=username, age=age)
    users.append(new_user)
    return new_user

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: int = Path(..., title="Enter User ID", ge=1, description="Enter User ID", example=1),
    username: str = Path(..., title="Enter username", min_length=5, max_length=20, description="Enter username", example="UrbanProfi"),
    age: int = Path(..., title="Enter age", ge=18, le=120, description="Enter age", example=28)
):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")

@app.delete("/user/{user_id}")
def delete_user(user_id: int = Path(..., title="Enter User ID", ge=1, description="Enter User ID", example=1)):
    for user in users:
        if user.id == user_id:
            users.remove(user)
            return user
    raise HTTPException(status_code=404, detail="User was not found")
