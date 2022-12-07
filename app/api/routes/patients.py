from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def get_all_patients():
    pass


@router.get('/{id}')
def get_patient(id: int):
    return {id}


@router.get('/{id}/doctors')
def get_patients_doctors(limit: int):
    return [i for i in range(limit)]


@router.delete('/{id}')
def delete_patient(id: int):
    return {id}


@router.patch('/{id}')
def update_patient(id: int, update_dto: object):
    return {id, *update_dto}


@router.post('/')
def delete_patient(dto):
    return {id, *dto}
