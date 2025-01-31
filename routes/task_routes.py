"""This module defines tasks blueprint"""
from flask import Blueprint, render_template, request, redirect, url_for
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
                deadline=datetime.strptime(deadline, '%Y-%m-%d') if deadline else None,
                user_id=current_user.id
                )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('task/create.html')


@tasks.route('/update', methods=('GET', 'PUT'))
@login_required
def update_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        priority = request.form.get('priority', 'Low')
        deadline = request.form.get('deadline')
        task = Task(
                title=title,
                description=description,
                priority=priority,
                deadline=datetime.strptime(deadline, '%Y-%m-%d') if deadline else None,
                user_id=current_user.id
                )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('users.dashboard'))

    return render_template('task.html')



@tasks.route('/delete/<int:id>', methods=('POST', ))
@login_required
def delete_task(id):
    task = Task.query.get_or_404(id)
    if task.owner != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('users.dashboard'))
