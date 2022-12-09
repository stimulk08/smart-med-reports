from fastapi import APIRouter
from app.api.quizzes.quizzes import router as quizzes_router
from app.api.doctors.doctors import router as doctors_router
from app.api.patients.router import router as patients_router
from app.api.chats.chats import router as chats_router
from app.api.tags.routes import router as tags_router

app_router = APIRouter()

app_router.include_router(quizzes_router, tags=['Quizzes'], prefix="/quizzes")
app_router.include_router(doctors_router, tags=['Doctors'], prefix="/doctors")
app_router.include_router(patients_router, tags=['Patients'], prefix="/patients")
app_router.include_router(chats_router, tags=['Chats'], prefix="/chats")
app_router.include_router(tags_router, tags=['Tags'], prefix="/tags")

