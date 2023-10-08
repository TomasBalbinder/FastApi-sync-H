from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.dialects.postgresql import ENUM  




class Cosmonaut(Base):
    __tablename__ = 'cosmonauts_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    gender = Column(ENUM("male", "female"))
