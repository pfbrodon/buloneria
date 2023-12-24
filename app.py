from flask import Flask
from routes.crud import crud


app = Flask(__name__)


# configuro la base de datos, con el nombre el usuario y la clave
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:12345678@localhost/buloneria"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # none
app.config["SECRET_KEY"] = "12345678"


app.register_blueprint(crud)


###################################################################
