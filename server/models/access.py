from datetime import datetime

from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Integer, String, DateTime

from models import Base

class Access(Base):
    __tablename__ = 'access'
    id = Column(Integer, primary_key=True)
    uuid = Column(String(36), ForeignKey('user.uuid'), index=True)
    page_id = Column(Integer, ForeignKey('page.id'), index=True)
    local_time = Column(DateTime, nullable=False)
    server_time = Column(DateTime, nullable=False, default=datetime.now())