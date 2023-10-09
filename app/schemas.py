from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Cosmonaut(BaseModel):
    id: Optional[UUID]
    name : str = Field(max_length=100)
    age : Optional[int]
    gender : Gender


class CosmonautUpdate(BaseModel):
    name : Optional[str]
    age : Optional[int]
    gender : Optional[Gender]