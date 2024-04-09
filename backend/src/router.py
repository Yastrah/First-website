from fastapi import APIRouter

router = APIRouter(
    # prefix="/something"
)

items_db = [{"item_name": "m1"}, {"item_name": "m2"}, {"item_name": "m3"}, {"item_name": "m4"}]

@router.get("/")
async def root():
    return {"message": "Hello World"}

@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}

@router.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@router.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

# http://127.0.0.1:8000/items?skip=1&limit=10
@router.get("/items")
async def read_item(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]
