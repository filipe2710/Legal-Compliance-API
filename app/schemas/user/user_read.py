from pydantic import BaseModel, ConfigDict
from datetime import date
from typing import List

class UserRead(BaseModel):
    model_config = ConfigDict(extra='forbid')
    id_user: str
    id_process: str
    name: str
    phone: str
    email: str
    gender: str
    cpf: str
    date_of_birth: date
    city: str
    created_at: date
    updated_at: List[date] | None = None
    
    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "id_user": "123e4567-e89b-12d3-a456-426614174000",
                "id_process": "123e4567-e89b-12d3-a456-426614174001",
                "name": "João Silva",
                "phone": "11999999999",
                "email": "joao.silva@example.com",
                "gender": "M",
                "cpf": "123.456.789-00",
                "date_of_birth": "1980-01-01",
                "city": "São Paulo",
                "created_at": "2023-01-01",
                "updated_at": ["2023-01-01"]
            }
        }
    )