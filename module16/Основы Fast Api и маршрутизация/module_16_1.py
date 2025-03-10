from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/")
def read_root()  -> dict:
    return {"message": "Главная страница"}

@app.get("/user/admin")
def read_admin() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
def read_user(user_id: int) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user")
def read_user_info(username, age):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
