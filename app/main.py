import uvicorn
from fastapi import FastAPI
from api.routes.routes import app_router


def bootstrap() -> FastAPI:
    application = FastAPI()
    application.include_router(app_router)
    return application


app = bootstrap()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

