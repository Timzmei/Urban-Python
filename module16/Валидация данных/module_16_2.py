from fastapi import FastAPI, Path, Annotated
from typing import Annotated

app = FastAPI()


@app.get("/user/{user_id}")
def read_user(user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, description="Enter User ID", example=1)]):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{username}/{age}")
def read_user_info(
    username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, description="Enter username", example="UrbanUser")],
    age: Annotated[int, Path(title="Enter age", ge=18, le=120, description="Enter age", example=24)]
):
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}
