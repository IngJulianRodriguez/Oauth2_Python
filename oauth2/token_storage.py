from cryptography.fernet import Fernet

class TokenStorage:
    def __init__(self, key):
        self.key = key
        self.cipher_suite = Fernet(key)

    def encrypt_token(self, token):
        return self.cipher_suite.encrypt(token.encode())

    def decrypt_token(self, encrypted_token):
        return self.cipher_suite.decrypt(encrypted_token).decode()

# Generar una clave y almacenarla de manera segura
key = Fernet.generate_key()
token_storage = TokenStorage(key)
