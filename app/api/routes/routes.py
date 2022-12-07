from fastapi import APIRouter
from .quizes import router as quizzes_router
from .doctors import router as doctors_router
from .patients import router as patients_router
from .chats import router as chats_router

app_router = APIRouter()

app_router.include_router(quizzes_router, tags=['Quizzes'], prefix="/quizzes")
app_router.include_router(doctors_router, tags=['Doctors'], prefix="/doctors")
app_router.include_router(patients_router, tags=['Patients'], prefix="/patients")
app_router.include_router(chats_router, tags=['Chats'], prefix="/chats")
