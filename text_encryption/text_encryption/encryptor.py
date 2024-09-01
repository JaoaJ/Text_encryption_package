from cryptography.fernet import Fernet

class TextEncryptor:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt(self, plaintext: str) -> str:
        encrypted_text = self.cipher_suite.encrypt(plaintext.encode())
        return encrypted_text.decode()

    def decrypt(self, encrypted_text: str) -> str:
        decrypted_text = self.cipher_suite.decrypt(encrypted_text.encode())
        return decrypted_text.decode()

    def get_key(self) -> str:
        return self.key.decode()
