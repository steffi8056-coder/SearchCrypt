from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"


def get_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

    else:
        with open(KEY_FILE, "rb") as file:
            key = file.read()

    return key


key = get_key()
cipher = Fernet(key)


def encrypt_data(data):
    return cipher.encrypt(data.encode()).decode()


def decrypt_data(data):
    return cipher.decrypt(data.encode()).decode()