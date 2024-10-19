import unittest
from oauth2_client import OAuth2Client

class TestOAuth2Client(unittest.TestCase):
    def setUp(self):
        self.client = OAuth2Client(
            client_id="test_client_id",
            client_secret="test_client_secret",
            auth_url="https://example.com/auth",
            token_url="https://example.com/token",
            redirect_uri="https://example.com/redirect"
        )

    def test_get_authorization_url(self):
        url = self.client.get_authorization_url(scope="test_scope")
        self.assertIn("response_type=code", url)
        self.assertIn("client_id=test_client_id", url)

    def test_get_token(self):
        # Aquí deberías usar un mock para simular la respuesta del servidor
        pass

    def test_refresh_token(self):
        # Aquí deberías usar un mock para simular la respuesta del servidor
        pass

if __name__ == '__main__':
    unittest.main()
