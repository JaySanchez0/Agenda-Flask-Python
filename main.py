from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes.Routes import routes
app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']="postgres://brkmiztteqwwyz:e1995d53aebe29fa561c0313df7a6ea0df211db26fb0550bce8be98ab1f41daa@ec2-107-21-214-26.compute-1.amazonaws.com:5432/d2a1nkrlpgcjf3"
routes(app)