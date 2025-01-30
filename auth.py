""" User authentication blueprint module """
import functools
from flask import (Blueprint, flash, g, redirect, render_template,
        request, session, url_for)
from werkzeug.security import check_password_hash, generate_password_hash
from models  import User
from models import db
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
# from app import app

# Authentication blueprint initialization
auth = Blueprint('auth', __name__, template_folder='templates/auth')

# Flask-Login inintialization
login_manager = LoginManager()
login_manager.session_protection = 'strong'
# login_manager.init_app(app)
login_manager.login_view = 'auth.login'
login_manager.login_message = "You're not signed in, login to access page."
bcrypt = Bcrypt()


@login_manager.user_loader
def load_user(user_id):
    for user in User.query.all():
        if str(user.id) == user_id:
            return user
    return None


@auth.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        # Retrieve data from form
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        error = None

        # Validate form data
        if not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif db.session.execute(db.select(User).filter_by(username=username)).scalar():
            error = 'Username is already taken.'
        elif db.session.execute(db.select(User).filter_by(email=email)).scalar():
            error = 'Email is already registered'

        # If no errors, hash the passowrd and save the user
        if error is None:
            hashed_passwd = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, email=email, password=hashed_passwd)
            try:    # Try if database error occurs
                db.session.add(new_user)
                db.session.commit()
                return redirect(url_for('auth.login'))
            except Exception as e:  # Rollback the session to avoid inconsistent state
                db.session.rollback()
                flash('An error occured while registering. Please try again.')
        else:
            flash(error)    # Flash the error message

    return render_template('register.html')


@auth.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        uname_email = request.form.get('username_or_email')
        password = request.form.get('password')
        error = None

        # Ensure user name and password is not empty
        if not uname_email or not password:
            error = 'Username/email and password are required.'
        else:
            # Fetch user by username or email
            user = (db.session.execute(db.select(User).filter(
                (User.username== uname_email) | (User.email == uname_email)
                )).scalar())

            # Validation
            if not user:
                error = 'Incorrect username or email.'
            elif not bcrypt.check_password_hash(user.password, password):
                error = 'Incorrect password.'

            # If no errors, log in the user
            if error is None:
                login_user(user)
                return redirect(url_for('auth.profile'))

        # Flash the error message
        flash(error)
    return render_template('login.html', user=current_user)


@auth.route('/profile', methods=('GET', ))
@login_required
def profile():
    return render_template('profile.html', user=current_user)


@auth.route('/logout', methods=('GET', ))
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))
