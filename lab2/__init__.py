from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://lab_qnus_user:LHpDeVulIwGqz6r2h7x6ehoeqe9tyx2S@dpg-cmc3cled3nmc73epdh00-a.oregon-postgres.render.com/lab_qnus"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import lab2.views
import lab2.models
