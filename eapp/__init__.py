from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager
import cloudinary
app = Flask(__name__)
app.secret_key = '&*(^UIGKJHJKHG&TFUTFYHGIUG&T*TUITGUIG&F'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@localhost/saledb?charset=utf8mb4"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config['PAGE_SIZE'] = 8
db = SQLAlchemy(app=app)
login = LoginManager(app = app)
cloudinary.config(cloud_name = 'y2myaui7', api_key ='162586493551941', api_secret = 'maEWNiUt4T0t4LT9cmiF98pYkPg')