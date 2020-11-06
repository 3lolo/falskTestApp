from flask import Blueprint

api_error_bp = Blueprint('api_error', __name__)

from app.autoria.api.errors import handlers
