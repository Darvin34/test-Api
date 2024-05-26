from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_database
import services as UserService
from data_transfer_objects import UserDTO

# Создание роутера и 4-ех эндпоинтов
router = APIRouter(tags=["user"])

@router.post('/')
async def create_user(data: UserDTO = None, database: Session = Depends(get_database)):
    return UserService.create_user(data, database)

@router.get('/{id}')
async def get(id: int = None, database: Session = Depends(get_database)):
    return UserService.get_user(id, database)

@router.put('/{id}')
async def update(data: UserDTO = None, database: Session = Depends(get_database), id: int = None):
    return UserService.update_user(data, database, id)

@router.delete('/{id}')
async def delete(id: int = None, database: Session = Depends(get_database)):
    return UserService.remove_user(database, id)