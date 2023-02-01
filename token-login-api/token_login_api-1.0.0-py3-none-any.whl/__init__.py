from .views import bp


class TokenLoginApi:

    def __init__(self, app=None, **kwargs):
        self.token_repository = kwargs.get('token_repository')
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.token_login_api = self
        app.register_blueprint(bp)
