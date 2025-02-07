"""This module defines users blueprint"""
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import User, Task, db
from datetime import datetime
 

users = Blueprint('users', __name__)


@users.route(f'/dashboard', methods=('GET', 'POST'))
@login_required
def dashboard():
    # tasks = Task.query.filter_by(user_id=current_user.id).all()
    tasks = Task.query.filter_by(user_id=current_user.id).order_by(Task.deadline).all()
    active = []
    behind = []
    completed = []
    for task in tasks:
        if task.deadline > datetime.now() and not task.completed:
            active.append(task)
        elif task.deadline < datetime.now() and not task.completed:
            behind.append(task)
        else:
            completed.append(task)

    return render_template('dashboard.html', tasks=tasks, active=active, behind=behind, completed=completed)

