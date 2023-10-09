from sqlalchemy import Column, Integer, String
from app.database import Base

class Cosmonaut(Base):
    __tablename__ = 'cosmonauts_table'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    gender = Column(String)
