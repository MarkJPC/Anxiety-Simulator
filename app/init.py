from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

# Create an instance of the Flask class
app = Flask(__name__)

# Set the secret key to protect against CSRF attacks
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

# Set the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# Create an instance of the database
db = SQLAlchemy(app)

# Create an instance of the Bcrypt class
bcrypt = Bcrypt(app)

# Create an instance of the LoginManager class
login_manager = LoginManager(app)

# Set the login view
login_manager.login_view = 'login'

# Set the login message category
login_manager.login_message_category = 'info'

# Import the routes module
from app import routes
