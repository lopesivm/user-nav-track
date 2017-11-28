from sqlalchemy import Column
from sqlalchemy.types import Integer, String, Text
from sqlalchemy.orm import relationship

from models import Base

class Page(Base):
    __tablename__ = 'page'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    url = Column(Text, nullable=False)
    accesses = relationship('Access', backref='page')