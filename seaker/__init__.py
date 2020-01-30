from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '63362f584ff66d1bda0281f6520bc914'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///seaker.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from seaker import routes