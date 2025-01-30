"""This module defines users blueprint"""
from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import User, db
from datetime import datetime

users = Blueprint('users', __name__)


@users.route(f'/users/dashboard', methods=('GET', 'POST'))
@login_required
def dashboard():
    if request.method == 'POST':
        pass

    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=tasks)

