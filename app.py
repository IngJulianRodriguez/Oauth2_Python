import json
from flask import Flask, redirect, request, session, url_for
from oauth2.oauth2_client import OAuth2Client
from oauth2.token_storage import TokenStorage
from cryptography.fernet import Fernet

app = Flask(__name__)
app.secret_key = 'your_secret_key'

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

# Crear almacenamiento de tokens
key = Fernet.generate_key()
token_storage = TokenStorage(key)

@app.route('/')
def index():
    if 'access_token' in session:
        return 'Logged in with token: ' + session['access_token']
    return redirect(url_for('login'))

@app.route('/login')
def login():
    auth_url = oauth_client.get_authorization_url(scope="email profile")
    return redirect(auth_url)

@app.route('/callback')
def callback():
    authorization_code = request.args.get('code')
    token_response = oauth_client.get_token(authorization_code)
    access_token = token_response['access_token']
    encrypted_token = token_storage.encrypt_token(access_token)
    session['access_token'] = encrypted_token
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
