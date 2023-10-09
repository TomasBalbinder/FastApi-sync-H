from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4, UUID
from enum import Enum


class Gender(str, Enum):
    male = 'male'
    female = 'female'


class Cosmonaut(BaseModel):
    id : UUID = uuid4()
    name : str = Field(max_length=10)
    age : Optional[int]
    gender : Gender


"""class CosmonautUpdate(BaseModel):
    name : Optional[str]
    age : Optional[int]
    gender : Optional[Gender]"""