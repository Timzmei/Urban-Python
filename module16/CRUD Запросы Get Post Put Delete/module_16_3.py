from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
user_id = 1

@app.get("/users")
def read_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(
    username: str = Path(..., title="Enter username", min_length=5, max_length=20, description="Enter username", example="UrbanUser"),
    age: int = Path(..., title="Enter age", ge=18, le=120, description="Enter age", example=24)
):
    global user_id
    user_id += 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(
    user_id: int = Path(..., title="Enter User ID", ge=1, le=100, description="Enter User ID", example=1),
    username: str = Path(..., title="Enter username", min_length=5, max_length=20, description="Enter username", example="UrbanProfi"),
    age: int = Path(..., title="Enter age", ge=18, le=120, description="Enter age", example=28)
):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: int = Path(..., title="Enter User ID", ge=1, le=100, description="Enter User ID", example=1)):
    if str(user_id) not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[str(user_id)]
    return f"User {user_id} has been deleted"
