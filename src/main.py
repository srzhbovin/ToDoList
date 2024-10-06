from fastapi import FastAPI
from src.api import include_routers
app = FastAPI(title='Fastapi ToDo List')
include_routers(app)

# MVC - Model, View, Controller

#GET /lists
#POST /lists
#DELETE /lists/{list_id}

#GET /lists/{list_id}/todos
#POST /lists/{list_id}/todos
#PATCH /lists/{list_id}/todos/{todo_id}
#DELETE /lists/{list_id}/todos/{todo_id}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)
