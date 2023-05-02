# from typing import Union
from fastapi import Depends, FastAPI
from typing import Annotated
# from pydantic import BaseModel
# from db import user_db, trade_db
# from models import Trade, User
from fastapi_users import FastAPIUsers

from auth.auth import auth_backend
import fastapi_users
from auth.schemas import UserCreate, UserRead, UserUpdate
from auth.database import User
from auth.manager import get_user_manager

app = FastAPI(
    title = 'trade'
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)   

current_active_user = fastapi_users.current_user(active=True)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)

@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}


# async def common_parameters(q: str | None = None, skip: int = 0, limit: int = 100):
#     return {"q": q, "skip": skip, "limit": limit}


# @app.get("/items/")
# async def read_items(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons


# @app.get("/users/")
# async def read_users(commons: Annotated[dict, Depends(common_parameters)]):
#     return commons

# @app.get('/users/{user_id}', response_model=list[User])
# def get_user(user_id: int):
#     return [user for user in user_db if user.get('id') == user_id]

# #Здесь вношу параметры, по умолчанию.
# @app.get('/trades/{user_id}')
# def get_trades(limit: int = 10, offset: int = 0):
#     return trade_db[offset:][:limit]

# @app.post('/users/{user_id}')
# def change_user_name(user_id: int, name: str):
#     current_user = list(filter(lambda user: user.get("id") == user_id, user_db))[0]
#     current_user['name'] = name
#     return {'status': 200, 'data': current_user}


# @app.post('/trades')
# def add_trades(trades: list[Trade]):
#     trade_db.extend(trades)
#     return {'status': 200, 'data': trade_db}
    


# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

