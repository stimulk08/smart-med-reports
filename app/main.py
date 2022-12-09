import uvicorn
from fastapi import FastAPI
from api import routes
from app.db.database import init_db


def bootstrap() -> FastAPI:
    application = FastAPI()
    init_db()
    application.include_router(routes.app_router)
    return application


app = bootstrap()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
