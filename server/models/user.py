from sqlalchemy import Column
from sqlalchemy.orm import relationship
from sqlalchemy.types import String

from models import Base

class User(Base):
    __tablename__ = 'user'
    uuid = Column(String(36), primary_key=True)
    email = Column(String(255))
    accesses = relationship('Access')