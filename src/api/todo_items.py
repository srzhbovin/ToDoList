from fastapi import APIRouter

router = APIRouter()


@router.get('/lists/{list_id}/todos')
async def get_todos():
    return


@router.post('/lists/{list_id}/todos')
async def create_todos():
    return


@router.post('/lists/{list_id}/todos')
async def delete_todos():
    return


@router.patch('/lists/{list_id}/todos/{todo_id}')
async def update_todo():
    return


@router.delete('/lists/{list_id}/todos/{todo_id}')
async def delete_todo():
    return
