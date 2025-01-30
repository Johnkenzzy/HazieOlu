#!/usr/bin/python3
"""This module defines the storage engine model for the Task Manager App"""
from flask_sqlalchemy import SQLAlchemy
from models.base_model import Base


# Create the database object
db = SQLAlchemy(model_class=Base)
