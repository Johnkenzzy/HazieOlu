"""Application initialization module"""
import os
from flask import Flask, render_template, jsonify, request, session
from models import Base, User, Task, db
from datetime import timedelta


user = os.getenv('USER', 'default_usr')
psswd = os.getenv('PWD', 'default_pwd')
host = os.getenv('HOST', 'localhost')
dbase = os.getenv('DB', 'default_db')

# App initialization and configuration
app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.getenv('SECRET_KEY')
app.config['SESSION_COOKIE_SECURE'] = True
app.config['REMEMBER_COOKIE_DURATION'] = timedelta(days=7)
app.config['DEBUG'] = True
# configure the MYSQL database, relative to the app instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, psswd, host, dbase)

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
