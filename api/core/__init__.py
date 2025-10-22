from flask import Flask
from flask_cors import CORS
from decouple import config

app = Flask(__name__)
CORS(app)  # 启用 CORS 支持
app.config.from_object(config("APP_SETTINGS", 
default='core.config.DevelopmentConfig'))

from core import routes
