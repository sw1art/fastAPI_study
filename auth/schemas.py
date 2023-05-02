from fastapi_users import schemas
from typing import Optional


class UserRead(schemas.BaseUser[int]):
    id: Optional[int]
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    age: Optional[int]
    email: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False
    
    class Config:
        orm_mode = True

class UserCreate(schemas.BaseUserCreate):
    username: Optional[str]
    firstname: Optional[str]
    lastname: Optional[str]
    age: Optional[int]
    email: Optional[str]
    password: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    password: Optional[str]
    email: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool]
    is_superuser: Optional[bool]
    is_verified: Optional[bool]