from fastapi import FastAPI

from src.router import router as router_blog

app = FastAPI()
# poetry run uvicorn src.main:app --reload

app.include_router(router_blog)
