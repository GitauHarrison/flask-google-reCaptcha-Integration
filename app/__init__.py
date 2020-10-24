from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)

bootstrap = Bootstrap(app)
db   = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

def start_ngrok():
    from pyngrok import ngrok

    url = ngrok.connect(5000)
    print(' * Tunnel URL:', url)

if app.config['START_NGROK']:
    start_ngrok()
    
from app import routes