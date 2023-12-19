from flask import Flask
from routes.crud import crud
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# configuro la base de datos, con el nombre el usuario y la clave
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:12345678@localhost/buloneria'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # none
#app.config["SECRET_KEY"] = "12345678"
SQLAlchemy(app)  # crea el objeto db de la clase SQLAlquemyb ,cvgb


app.register_blueprint(crud)





###################################################################


