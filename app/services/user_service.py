from typing import List, Optional
from datetime import date
from uuid import uuid4

from app.schemas.user.user_create import User
from app.schemas.user.user_read import UserRead

class UserService:
    def __init__(self):
        self.users: List[UserRead] = []

    def create_user(self, user_data: User) -> UserRead:
        
        if not self._validate_if_update_is_valid(data_after=user_data, data_updated=user_data, id_process=user_data, tolerance=30):
            raise ValueError("Invalid update: The created_at date cannot be modified or must be within the allowed tolerance period.")
    
        user = UserRead(
            id_user=str(uuid4()),
            id_process=user_data.id_process,
            name=user_data.name,
            phone=user_data.phone,
            email=user_data.email,
            gender=user_data.gender,
            cpf=user_data.cpf,
            date_of_birth=user_data.date_of_birth,
            city=user_data.city,
            created_at=date.today(),
            updated_at=None
        )
        self.users.append(user)
        return user

    def get_user(self, user_id: str) -> Optional[UserRead]:
        for user in self.users:
            if user.id_user == user_id:
                return user
        return None

    def list_users(self) -> List[UserRead]:
        return [self.get_user(user.id_user) for user in self.users]
    
    def get_client_by_id(self, user_id: str) -> Optional[UserRead]:
        for user in self.users:
            if user.id_user == user_id:
                return UserRead(
                    id_user=user.id_user,
                    name=user.name,
                    email=user.email,
                    city=user.city
                )
        return None
      
    def get_clients_by_city(self, city: str) -> List[UserRead]:
      for user in self.users:
          if user.city == city:
              return UserRead(
                  id_user=user.id_user,
                  name=user.name,
                  email=user.email,
                  city=user.city
              )
      return []
    
    def delete_user(self, user_id: str) -> bool:
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
      
    def put_user_by_id(self, user_id: str, user_data: User) -> Optional[UserRead]:
        for index, user in enumerate(self.users):
            if user.id_user == user_id:
                updated_user = UserRead(
                    id_user=user.id_user,
                    id_process=user.id_process,
                    name=user_data.name,
                    phone=user_data.phone,
                    email=user_data.email,
                    gender=user_data.gender,
                    cpf=user_data.cpf,
                    date_of_birth=user_data.date_of_birth,
                    city=user_data.city,
                    created_at=user.created_at,
                    updated_at=[date.today()]
                )
                self.users[index] = updated_user
                return updated_user
        return None

    
    def patch_user_by_id(self, user_id: str, user_data: User) -> Optional[UserRead]:
        for index, user in enumerate(self.users):
            if user.id_user == user_id:
                updated_user = self.users[index]
                if user_data.name is not None:
                    updated_user.name = user_data.name
                if user_data.email is not None:
                    updated_user.email = user_data.email
                if user_data.city is not None:
                    updated_user.city = user_data.city
                self.users[index] = updated_user
                return UserRead(
                    id_user=updated_user.id_user,
                    name=updated_user.name,
                    email=updated_user.email,
                    city=updated_user.city
                )
        return None
    
    def get_users_by_birth_date_range(self, start_date: date, end_date: date) -> List[UserRead]:
        users_in_range = []
        for user in self.users.values():
            if start_date <= user.date_of_birth <= end_date:
                users_in_range.append(UserRead(
                    id_user=user.id_user,
                    name=user.name,
                    email=user.email,
                    city=user.city
                ))
        return users_in_range   
    
    def _validate_if_update_is_valid(self, data_after: UserRead, data_updated: UserRead, id_process: UserRead, tolerance: int) -> bool:
        if data_after.created_at != data_updated.created_at:
            return True
        if data_after.created_at >= data_updated.created_at:
            return 
        if data_after.created_at <= data_updated.created_at and (data_updated.created_at - data_after.created_at).days > tolerance:
            return True
        
        id_process = id_process.updated_at.index(data_updated.created_at [+1])
        
        