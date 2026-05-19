from pydantic import BaseModel, field_validator, ConfigDict
from datetime import date
from typing import Literal
import re

class User(BaseModel):
    model_config = ConfigDict(extra='forbid')
    name: str
    phone: str
    email: str
    gender: Literal["Masculino", "Feminino"]
    cpf: str
    date_of_birth: date
    city: Literal["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Curitiba", "Recife", "Porto Alegre", "Manaus"]

    model_config = ConfigDict(
        extra='forbid',
        json_schema_extra={
            "example": {
                "name": "João Silva",
                "phone": "(11) 91234-5678",
                "email": "joao.silva@example.com",
                "gender": "Masculino",
                "cpf": "123.456.789-00",
                "date_of_birth": "1990-01-01",
                "city": "São Paulo"
            }
        }
    )

    @field_validator('email', mode='before')
    @classmethod
    def validate_email(cls, value):
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, value):
            raise ValueError('Invalid email format')
        return value
      
    @field_validator('phone', mode='before')
    @classmethod
    def validate_phone(cls, value):
        phone_regex = r'^\(\d{2}\) \d{4,5}-\d{4}$'
        if not re.match(phone_regex, value):
            raise ValueError('Invalid phone format')
        return value
      
    @field_validator('gender', mode='before')
    @classmethod
    def validate_gender(cls, value):
        value = value.strip().lower().capitalize()
      
        if value not in ["Masculino", "Feminino"]:
            raise ValueError('Invalid gender')
        return value

    @field_validator('cpf', mode='before')
    @classmethod
    def validate_cpf(cls, value):
        cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        if not re.match(cpf_regex, value):
            raise ValueError('Invalid CPF format')
        return value

    @field_validator('city', mode='before')
    def validate_city(cls, value):
        value = value.strip().capitalize()
      
        if not value:
            raise ValueError('City is required')
        return value