import json
from oauth2_client import OAuth2Client

# Cargar configuración
with open('config.json') as config_file:
    config = json.load(config_file)

# Seleccionar proveedor (por ejemplo, Google)
provider = config['google']

# Crear cliente OAuth2
oauth_client = OAuth2Client(
    client_id=provider['client_id'],
    client_secret=provider['client_secret'],
    auth_url=provider['auth_url'],
    token_url=provider['token_url'],
    redirect_uri=provider['redirect_uri']
)

# Obtener URL de autorización
auth_url = oauth_client.get_authorization_url(scope="email profile")
print(f"Visita esta URL para autorizar la aplicación: {auth_url}")

# Después de autorizar, obtener el código de autorización y canjearlo por un token
authorization_code = input("Introduce el código de autorización: ")
token_response = oauth_client.get_token(authorization_code)
print(f"Access Token: {token_response['access_token']}")
