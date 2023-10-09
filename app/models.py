from sqlalchemy import Column, String, UUID
from app.database import Base
import uuid


class Cosmonaut(Base):
    __tablename__ = 'cosmonauts_table'

    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True, index=True)
    name = Column(String)
    age = Column(String)
    gender = Column(String)
