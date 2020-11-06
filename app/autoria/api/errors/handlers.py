from app.autoria.api.errors import api_error_bp as api_error
from app.autoria.api.errors import errors as api_error_response


@api_error.app_errorhandler(400)
def not_found_error(error):
    return api_error_response.error_response(400)


@api_error.app_errorhandler(404)
def not_found_error_404(error):
    return api_error_response.error_response(404)


@api_error.app_errorhandler(500)
def not_found_error_500(error):
    return api_error_response.error_response(500)
