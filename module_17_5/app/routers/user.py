from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.backend.db_depends import get_db
from typing import Annotated
from app.models.user import User
from app.models.task import Task
from app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix="/user", tags=["user"])

@router.get("/")
async def all_users(db: Annotated [Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

@router.get("/{user_id}")
async def user_by_id(db: Annotated [Session, Depends(get_db)],
                     user_id: int):
    user = db.scalar(select(User).where(User.id==user_id))
    if user is not None:
        return user
    raise HTTPException(status_code=404, detail="User was not found")

@router.post("/create")
async def create_user(db: Annotated[Session, Depends(get_db)],
                      user_create_model: CreateUser):
    db_user = User(**user_create_model.dict(), slug=slugify(user_create_model.username))
    db.add(db_user)
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}

@router.put("/update")
async def update_user(db: Annotated[Session, Depends(get_db)],
                      user_id: int,
                      user_update_model: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(update(User).where(User.id == user_id).values(
            firstname=user_update_model.firstname,
            lastname= user_update_model.lastname,
            age=user_update_model.age,
        ))
        db.commit()

        return {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
    raise HTTPException(status_code=404, detail="User was not found")

@router.get("/user_id/tasks")
async def tasks_by_user_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    tasks = list(db.scalar(select(Task).where(Task.id==user_id)))
    return tasks


@router.delete("/delete")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
    task = db.scalar(select(Task).where(Task.user_id == user_id))
    if task is not None:
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.commit()
        return {'status_code': status.HTTP_204_NO_CONTENT, 'transaction': 'User deleted successfully!'}
    raise HTTPException(status_code=404, detail="User was not found")