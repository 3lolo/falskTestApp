from flask import Flask
from config import Config

# from app.autoria.api.config import Config as AutoriaConfig

app = Flask(__name__)

# app.config.from_object(Config)
# app.config.from_object(AutoriaConfig)
from app import routes

from app.autoria.api import auto_bp as auto_ria_api
from app.autoria.api.errors import api_error_bp as auto_ria_api_error

app.register_blueprint(auto_ria_api, url_prefix='/api/auto')
app.register_blueprint(auto_ria_api_error)
