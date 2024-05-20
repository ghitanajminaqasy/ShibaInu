'''
This file contains SQLAlchemy models. 
If you looking for Pydantic models, you can find it in schemas/room_schemas.py

'''
import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy_utils import UUIDType
import uuid

from database.database import DBServerWrites

class PendinginRuangan(DBServerWrites.Base):
    __tablename__ = "pendingin_ruangan"

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, index=True)
    location = Column(String, index=True)
    status = Column(String, index=True)

    create_at = Column(DateTime, default=func.now())
    update_at = Column(DateTime, default=func.now(), onupdate=func.now())
