from fastapi import FastAPI
from api.routes.routes import app_router


def bootstrap() -> FastAPI:
    application = FastAPI()
    application.include_router(app_router)
    return application


app = bootstrap()
