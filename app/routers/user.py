from fastapi import APIRouter

router = APIRouter(prefix = "/user", tags = ["user"])

@router.get ('/')
async def all_users():
    pass

@router.get ('/user_id')
async def user_by_id():
    pass

@router.post ('/user_id')
async def create_user():
    pass

@router.post ('/update')
async def update_user():
    pass

@router.post ('/delete')
async def delete_user():
    pass

