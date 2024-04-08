from fastapi import APIRouter

router = APIRouter(
    # prefix="/something"
)

@router.get("/")
async def root():
    return {"message": "Hello World"}