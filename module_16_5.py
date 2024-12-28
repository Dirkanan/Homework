from fastapi import FastAPI, HTTPException, Path, Request
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from typing import Annotated, List
from fastapi.responses import HTMLResponse

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
templates = Jinja2Templates(directory="module_16/templates")
users = []


class User(BaseModel):
    id: int
    username: str
    age: int

@app.get("/", response_class = HTMLResponse)
async def read_users(request: Request):
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


@app.get('/users/{user_id}', response_class=HTMLResponse)
async def get_user(request: Request, user_id: int = Path(..., title="The ID of the user to get")):
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username", )],
        age: Annotated[int, Path(ge=18, le=120, description="Enter age")]):
    user_id = (users[-1].id + 1) if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return f"User {new_user} is registered"


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: Annotated[int, Path(gt=0, description="User ID must be greater than 0")],
    username: Annotated[str, Path(min_length=5, max_length=20, description="Enter username")],
    age: Annotated[int, Path(ge=18, le=120, description="Enter age")],):

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: Annotated[int, Path(gt=0, description="User ID must be greater than 0")]):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user
    raise HTTPException(status_code=404, detail="User was not found")
