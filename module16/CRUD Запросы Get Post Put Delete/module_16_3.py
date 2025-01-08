from fastapi import FastAPI, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}
user_id = 1

@app.get("/users")
def read_users():
    return users

@app.post("/user/{username}/{age}")
def create_user(username: str, age: int):
    global user_id
    user_id += 1
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} is registered"

@app.put("/user/{user_id}/{username}/{age}")
def update_user(user_id: str, username: str, age: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"

@app.delete("/user/{user_id}")
def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"