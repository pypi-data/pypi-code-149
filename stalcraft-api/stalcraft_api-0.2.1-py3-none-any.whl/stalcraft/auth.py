import requests
import uuid


class Authorization:
    AUTHORIZE_URL = "https://exbo.net/oauth/authorize"
    TOKEN_URL = "https://exbo.net/oauth/token"
    USER_URL = "https://exbo.net/oauth/user"

    def __init__(self, client_id: str, client_secret: str, scope="", redirect_uri: str = "http://localhost"):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.state = ""

        self.code = ""

    def get_user_code(self):
        self.state = uuid.uuid4().hex
        return f"{self.AUTHORIZE_URL}?client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={self.scope}&response_type=code&state={self.state}"

    def input_code(self):
        self.code = input("Enter the authorization code from the redirect URL: ")

    def get_user_token(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "code": self.code,
            "grant_type": "authorization_code",
            "redirect_uri": self.redirect_uri,
            "state": self.state
        }

        response = requests.post(self.TOKEN_URL, data=data)

        return response.json()

    def get_app_token(self):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
            "scope": self.scope
        }

        response = requests.post(self.TOKEN_URL, data=data)

        return response.json()

    def update_token(self, refresh_token: str):
        data = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "refresh_token",
            "refresh_token": refresh_token,
            "scope": self.scope
        }

        response = requests.post(self.TOKEN_URL, data=data)

        return response.json()

    def info(self, token: str):
        headers = {
            "Authorization": f"Bearer {token}"
        }

        response = requests.get(self.USER_URL, headers=headers)

        return response.json()
