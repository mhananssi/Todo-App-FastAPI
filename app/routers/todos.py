from fastapi import APIRouter, status, HTTPException, Request, Depends
from app.database.todo.schema import CreateTodoItem
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


@router.get('/all', response_model=list, status_code=status.HTTP_200_OK)
async def get_all_todoitems(request: Request):
    user_id = request.state.user_id
    items = services.get_all_todoitems(user_id)
    items.sort(key=lambda item: item.due_date)
    return items
