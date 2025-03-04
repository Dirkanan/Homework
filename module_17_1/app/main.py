from fastapi import FastAPI, APIRouter
from app.routers.task import router as task_router
from app.routers.user import router as user_router

app = FastAPI()

@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Подключаем маршруты
app.include_router(task_router)
app.include_router(user_router)