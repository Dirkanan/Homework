from fastapi import FastAPI
from routers import task, user
from db import Base, engine
from app.models import *

Base.metadata.create_all(bind=engine)

@app.get ("/")
async def chill_boy():
    return {"message" : "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)




