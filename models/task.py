#!/usr/bin/python3
"""
This module defines the Task class for the Task Manager App
"""
from models.base_model import BaseModel
from sqlalchemy import String, DateTime, Boolean, Text, Uuid, ForeignKey
from sqlalchemy.orm import mapped_column
from models.engine_model import db
# from flask_sqlalchemy import SQLAlchemy


# db = SQLAlchemy(model_class=Base)


class Task(BaseModel, db.Model):
    """Defines the Task attributes"""
    __tablename__ = 'tasks'
    title = mapped_column(String(128), nullable=False)
    description = mapped_column(Text, nullable=True)
    priority = mapped_column(String(10), nullable=False, default='Low')  # Low, Medium, High
    deadline = mapped_column(DateTime, nullable=True)
    completed = mapped_column(Boolean, default=False)
    user_id = mapped_column(Uuid, ForeignKey('users.id'), nullable=False)


if __name__ == '__main__':
    task = Task(title='Study', description='Nil', deadline='6pm', priority='Low')
    print(task.id)
    print(task.created_at)
    print(task.updated_at)
    print(task.title)
    print(task.description)
    print(task.priority)
    print(task.deadline)
    print(task.completed)
    print(task.user_id)
