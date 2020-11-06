from app.autoria.api import auto_bp
from flask import jsonify


@auto_bp.route('/list', methods=['GET'])
def get_autos_list():
    pass


@auto_bp.route('/')
def home():
    return jsonify(username="g.user.username",
                   email="g.user.email",
                   id="g.user.id")
