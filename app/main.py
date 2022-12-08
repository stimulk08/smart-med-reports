import uvicorn
from fastapi import FastAPI
from api import app_router
from app.db.database import Database, engine


def bootstrap() -> FastAPI:
    application = FastAPI()
    Database.metadata.create_all(engine)
    application.include_router(app_router)
    return application


app = bootstrap()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
