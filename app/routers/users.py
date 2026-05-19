from fastapi import APIRouter, HTTPException, status

from ..schemas.user.user_create import User
from ..schemas.user.user_read import UserRead
from ..services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])

user_service = UserService()

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    try:
        return user_service.create_user(user)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e)) 
      
@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: str):
    user = user_service.get_user(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
  
@router.get("/", response_model=list[UserRead])
def list_users():
    return user_service.list_users()
  
@router.get("/id/{user_id}", response_model=UserRead)
def get_user_by_id(user_id: str):
    user = user_service.get_client_by_id(user_id)
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user
  
@router.get("/city/{city}", response_model=list[UserRead])
def get_users_by_city(city: str):
    return user_service.get_clients_by_city(city)
  
@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: str):
    if not user_service.delete_user(user_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
      
@router.put("/{user_id}", response_model=UserRead)
def put_user(user_id: str, user_data: User):
    try:
        updated_user = user_service.put_user_by_id(user_id, user_data)
        if updated_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
      
@router.patch("/{user_id}", response_model=UserRead)
def patch_user(user_id: str, user_data: User):
    try:
        updated_user = user_service.patch_user_by_id(user_id, user_data)
        if updated_user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return updated_user
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
      
@router.get("/birthday/{date}", response_model=list[UserRead])
def get_users_by_birthday(date: str):
    return user_service.get_users_by_birth_date_range(date)
  