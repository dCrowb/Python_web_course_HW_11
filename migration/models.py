
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from sqlalchemy.orm import declarative_base

from src.db.db import engine

Base = declarative_base()


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    birthday = Column(DateTime)
    email = Column(String(150), unique=True, nullable=False)
    phone = Column(String(30), unique=True, nullable=False)
    favorite = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), updated_at=func.now())


Base.metadata.create_all(bind=engine)