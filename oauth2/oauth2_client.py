import requests
from requests.auth import HTTPBasicAuth

class OAuth2Client:
    def __init__(self, client_id, client_secret, auth_url, token_url, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.auth_url = auth_url
        self.token_url = token_url
        self.redirect_uri = redirect_uri

    def get_authorization_url(self, scope):
        return f"{self.auth_url}?response_type=code&client_id={self.client_id}&redirect_uri={self.redirect_uri}&scope={scope}"

    def get_token(self, authorization_code):
        data = {
            'grant_type': 'authorization_code',
            'code': authorization_code,
            'redirect_uri': self.redirect_uri,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.token_url, data=data, auth=HTTPBasicAuth(self.client_id, self.client_secret))
        return response.json()

    def refresh_token(self, refresh_token):
        data = {
            'grant_type': 'refresh_token',
            'refresh_token': refresh_token,
            'client_id': self.client_id,
            'client_secret': self.client_secret
        }
        response = requests.post(self.token_url, data=data, auth=HTTPBasicAuth(self.client_id, self.client_secret))
        return response.json()
