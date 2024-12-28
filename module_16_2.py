from fastapi import FastAPI, Path, Query
from typing import Annotated

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def read_user(user_id: Annotated[int, Path(ge=1, le=100, description="Enter User ID", )]):
    return {"user_id": user_id}


@app.get("/user/{username}/{age}")
async def read_user_info(
        username: Annotated[str, Path( min_length=5, max_length=20, description="Enter username",)],
        age: Annotated[int, Path( ge=18, le=120, description="Enter age")]):
    return {"username": username, "age": age}