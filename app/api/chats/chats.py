from fastapi import APIRouter

router = APIRouter()


@router.get('/')
def get_all_chats(participant_id: int, limit: int):
    pass


@router.get('/{id}')
def get_chat(id: int):
    return {id}


@router.delete('/{id}')
def delete_chat(id: int):
    return {id}


@router.patch('/{id}')
def update_chat(id: int, update_dto: object):
    return {id, *update_dto}


@router.post('/')
def delete_chat(dto):
    return {id, *dto}
