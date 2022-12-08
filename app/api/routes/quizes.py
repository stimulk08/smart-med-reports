from fastapi import APIRouter, Depends

router = APIRouter(prefix="/quizzes")


@router.get('/')
def get_all_quizzes():
    return "Quiz"


@router.get('/{id}')
def get_quiz(id: int):
    return {id}


@router.delete('/{id}')
def delete_quiz(id: int):
    return {id}


@router.patch('/{id}')
def update_quiz(id: int, update_dto: object):
    return {id, *update_dto}


@router.post('/')
def delete_quiz(dto):
    return {id, *dto}
