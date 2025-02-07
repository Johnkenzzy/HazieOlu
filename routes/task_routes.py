"""This module defines tasks blueprint"""
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from flask_login import login_required, current_user
from models import Task, db
from datetime import datetime


tasks = Blueprint('tasks', __name__)


@tasks.route('/create', methods=('GET', 'POST'))
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description', None)
        priority = request.form.get('priority', 'Low')
        deadline = request.form.get('deadline')
        task = Task(
                title=title,
                description=description,
                priority=priority,
                deadline=datetime.strptime(deadline, '%Y-%m-%dT%H:%M') if deadline else None,
                user_id=current_user.id
                )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('task/create.html', task=None)


@tasks.route('/update/<task_id>', methods=('GET', 'POST'))
@login_required
def update_task(task_id):
    task_id = uuid.UUID(task_id)
    task = Task.query.get_or_404(task_id)
    
    if request.method == 'POST':
        task.title = request.form.get('title')
        task.description = request.form.get('description', None)
        task.priority = request.form.get('priority', 'Low')
        
        deadline = request.form.get('deadline')
        task.deadline = datetime.strptime(deadline, '%Y-%m-%dT%H:%M') if deadline else None
        
        task.updated_at = datetime.now()

        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('task/create.html', task=task) 


@tasks.route('/delete/<task_id>', methods=('GET', ))
@login_required
def delete_task(task_id):
    task_id = uuid.UUID(task_id)
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('users.dashboard'))


@tasks.route('/update_complete/<task_id>', methods=('POST', ))
@login_required
def update_complete(task_id):
    task_id = uuid.UUID(task_id)
    task = Task.query.get(task_id)

    if not task:
        return "Task not found", 404

    # Update task completion status based on form data
    task.completed = "completed" in request.form
    db.session.commit()

    return redirect(url_for('users.dashboard'))
