"""Application initialization module"""
import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify, request, session
from models import Base, User, Task, db
from datetime import timedelta

# Load environment variables
load_dotenv()

# App initialization
app = Flask(__name__, instance_relative_config=True)

# App configuration
app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

# Database initialization
db.init_app(app)
with app.app_context():
    db.create_all()

from routes import login_manager, auth
login_manager.init_app(app)
app.register_blueprint(auth, url_prefix='/auth')

from routes import users
app.register_blueprint(users, url_prefix='/users')

from routes import tasks
app.register_blueprint(tasks, url_prefix='/tasks')


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        data = request.get_json()
        user = User(username=data['name'], password=data['pass'], email=data['email'])
        db.session.add(user)
        db.session.commit()
        users = User.query.all()
        return jsonify([{"id": user.id, "name": user.username, "email": user.email} for user in users])
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
