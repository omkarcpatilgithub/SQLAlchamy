from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String

app = Flask(__name__)
## link for sql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@127.0.0.1:3306/employee'

## instantiate db object
db = SQLAlchemy(app)

## set mapping to a table
class Example(db.Model):
    __tablename__ = 'person'
    id = db.Column('id', db.Integer, primary_key = True)
    username = db.Column('username', db.Unicode)

    def __init__(self, id, username):
        self.id = id
        self.username = username

