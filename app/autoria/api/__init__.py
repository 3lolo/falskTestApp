from flask import Blueprint

auto_bp = Blueprint('api', __name__)

from app.autoria.api import auto_routs
