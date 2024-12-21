from fastapi import FastAPI, HTTPException, Path
from typing import Annotated
app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users

@app.post("/user/{username}/{age}")
async def create_user(
        username: Annotated[str, Path( min_length=5, max_length=20, description="Enter username",)],
        age: Annotated[int, Path( ge=18, le=120, description="Enter age")]):
    new_user_id = str(max(int(k) for k in users.keys()) + 1)
    users[new_user_id] = f"Имя: {username}, возраст: {age}"
    return f"User {new_user_id} is registered"



@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path( min_length=1, max_length=3, description="Enter username",)],
        username: Annotated[str, Path( min_length=5, max_length=20, description="Enter username",)],
        age: Annotated[int, Path( ge=18, le=120, description="Enter age")]):
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[str, Path( min_length=1, max_length=3, description="Enter username",)],
        username: Annotated[str, Path( min_length=5, max_length=20, description="Enter username",)],
        age: Annotated[int, Path( ge=18, le=120, description="Enter age")]):
    try:
        users[user_id] = f"Имя: {username}, возраст: {age}"
        return f"User {user_id} has been updated"
    except IndexError:
        if user_id not in users:
            raise HTTPException(status_code=404, detail="User not found")


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    del users[user_id]
    return f"User {user_id} has been deleted"
