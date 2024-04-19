from fastapi import APIRouter, Query, Depends
from pydantic import BaseModel


from typing import Union, Annotated

class SAdvert(BaseModel):
    id: int
    title: str
    author: str
    description: str
    # tax: Union[float, None] = None


router = APIRouter(
    prefix="/advert"
)

# items_db = [{"item_name": "m1"}, {"item_name": "m2"}, {"item_name": "m3"}, {"item_name": "m4"}]

# @router.get("/")
# async def root():
#     return {"message": "Hello World"}

# @router.get("/items/{item_id}")
# async def read_item(item_id: int):
#     return {"item_id": item_id}

# @router.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @router.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

# http://127.0.0.1:8000/items?skip=1&limit=10
# @router.get("/items")
# async def read_item(skip: int, limit: int = 10):  # skip - required, limit - optional
#     return items_db[skip: skip + limit]

adverts = []

@router.post("/")
async def create_advert(
        advert: Annotated[SAdvert, Depends()]
):
    adverts.append(advert)
    return {"ok": True, "advert_id": len(adverts)}


@router.get("/")
async def get_advert() -> list[SAdvert]:
    return adverts

# @router.put("/items/{item_id}")
# async def update_item(item_id: int, item: SItem):
#     return {"item_id": item_id, **item.dict()}

# @router.get("/items/")
# async def read_items(
#     q: Annotated[
#         Union[str, None], Query(min_length=3, max_length=50, pattern=r"^fixedquery$")
#     ] = None,
# ):
#     results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

