from fastapi import FastAPI

from src.router import router as router_blog

app = FastAPI()

app.include_router(router_blog)
