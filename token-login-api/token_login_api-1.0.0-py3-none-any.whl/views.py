from flask import Blueprint, current_app as app, request, jsonify


bp = Blueprint('token_login_api', __name__, url_prefix='/token-login-api')


@bp.post('/valid-login')
def valid_login():
    result = app.token_login_api.token_repository.get_by_username(
        request.form['username'])
    return jsonify(
        {'is_valid': True if result == request.form['token'] else False})
