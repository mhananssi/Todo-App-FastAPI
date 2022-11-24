from fastapi import APIRouter, status, HTTPException, Request, Depends
from app.database.todo.schema import CreateTodoItem, UpdateTodoItem
from app.database.todo import services
from app.extensions import authorize

router = APIRouter(dependencies=[Depends(authorize)])


@router.post('/add-item', response_model=dict, status_code=status.HTTP_201_CREATED)
async def add_todoitem(request: Request, item: CreateTodoItem):
    user_id = request.state.user_id
    db_item = services.get_item(user_id, item.title, item.due_date)
    if db_item:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Item already exists.')
    db_item = services.create_item(user_id, item)
    return {'Success': 'Todo Item added successfully.', 'Item': db_item}


@router.put('/update-item/{item_id}', response_model=dict, status_code=status.HTTP_200_OK)
async def update_todoitem(request: Request, item_id: int, item: UpdateTodoItem):
    user_id = request.state.user_id
    db_item = services.item_exits(item_id)
    if not db_item or db_item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found.')
    services.update_item(item_id, item)
    return {'Success': 'Todo Item updated successfully.'}


@router.get('/all', response_model=list, status_code=status.HTTP_200_OK)
async def get_all_todoitems(request: Request):
    user_id = request.state.user_id
    items = services.get_all_todoitems(user_id)
    items.sort(key=lambda item: item.due_date)
    return items


@router.delete('/delete-item/{item_id}', response_model=dict, status_code=status.HTTP_200_OK)
async def delete_todoitem(request: Request, item_id: int):
    user_id = request.state.user_id
    db_item = services.item_exits(item_id)
    if not db_item or db_item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found.')
    services.delete_item(item_id)
    return {'Success': 'Item deleted successfully.'}


@router.put('/done/{item_id}', response_model=dict, status_code=status.HTTP_200_OK)
async def mark_todoitem_done(request: Request, item_id: int):
    user_id = request.state.user_id
    db_item = services.item_exits(item_id)
    if not db_item or db_item.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found.')
    services.mark_done(item_id)
    return {'Success': 'Todo Item marked done.'}


@router.get('/all-done', response_model=list, status_code=status.HTTP_200_OK)
async def get_all_done_todoitems(request: Request):
    user_id = request.state.user_id
    items = services.get_all_done_items(user_id)
    items.sort(key=lambda item: item.due_date)
    return items


@router.get('/due-today', response_model=list, status_code=status.HTTP_200_OK)
async def get_todoitems_due_today(request: Request):
    user_id = request.state.user_id
    items = services.get_items_due_today(user_id)
    items.sort(key=lambda item: item.due_date)
    return items
