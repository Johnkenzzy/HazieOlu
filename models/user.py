#!/usr/bin/python3
"""
This module defines the User class for the Task Manager App
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, mapped_column
from flask_login import UserMixin
from models.engine_model import db
from uuid import UUID


class User(BaseModel, db.Model, UserMixin):
    """User class attributes declaration"""
    __tablename__ = 'users'
    username = mapped_column(String(128), nullable=True, unique=True)
    password = mapped_column(String(128), nullable=False)
    email = mapped_column(String(128), nullable=False, unique=True)
    tasks = relationship(
            'Task', backref='owner',
            cascade='all, delete-orphan'
            )

    @classmethod
    def get(cls, user_id):
        user = User.query.filter_by(id=UUID(user_id)).first()
        return user


if __name__ == '__main__':
    inst = User(username='Johnkennedy', password='12345', email='johnkenumeh@gmail.com')
    print(inst.id)
    print(inst.created_at)
    print(inst.updated_at)
    print(inst.username)
    print(inst.password)
    print(inst.email)
