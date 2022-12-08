from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def get_all_doctors():
    pass


@router.get('/{id}')
def get_doctor(id: int):
    return {id}


@router.get('/{id}/patients')
def get_doctors_patients(limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_doctor(id: int):
    return {id}


@router.patch('/{id}')
def update_doctor(id: int, update_dto: object):
    return {id, *update_dto}


@router.post('/')
def delete_doctor(dto):
    return {id, *dto}
