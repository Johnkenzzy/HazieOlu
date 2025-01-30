#!/usr/bin/python3
"""
This module defines the base class for Task Manager App models
"""
import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import String, DateTime, Uuid
from sqlalchemy.orm import mapped_column
from datetime import datetime


# Base = declarative_base()
class Base(DeclarativeBase):
    """A class-based approach that declare sqlalchemy base class explicitly"""
    pass


class BaseModel:
    """The base class model for common attributes initialization"""
    id = mapped_column(Uuid, nullable=False, primary_key=True)
    created_at = mapped_column(DateTime, nullable=False,
            default=datetime.utcnow())
    updated_at = mapped_column(DateTime, nullable=False,
            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatnces initialization"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            self.__dict__.update(kwargs)



if __name__ == '__main__':
    instance = BaseModel()
    print(instance.id)
    print(instance.created_at)
    print(instance.updated_at)
