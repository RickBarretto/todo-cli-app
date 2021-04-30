import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from .file_io import File

class Passcode:

    def create(passcode:str) -> tuple[bytes]:

        passcode = bytes(passcode.encode())
        salt = os.urandom(64)
        
        return passcode, salt

    def store_passcode(key:bytes) -> None:
        path = r""
        File.write("secret", "key", path, key)

    def verify_passcode(passcode_try:str, key:bytes):

        salt = os.urandom(64)

        result = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                 ).verify(passcode.encode(), key)

        return result


class Crypt:

    def generate_key(passcode:bytes, salt:bytes) -> bytes:

        key = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=default_backend()
                 ).derive(passcode)

        return key


    def en(key:bytes, salt:bytes, arg:str):

        nonce = salt

        aesgcm = AESGCM(key)
        encripted:bytes = aesgcm.encrypt(
            nonce=nonce,
            data=arg.encode(),
            associated_data=None            
        )

        encripted:bytes = base64.urlsafe_b64encode(encripted)
        return encripted




    def de(key:bytes, arg:bytes) -> str:

        aesgcm = AESGCM(key)

        decrypted:bytes = aesgcm.decrypt(
            nonce=nonce,
            data=base64.urlsafe_b64decode(arg),
            associated_data=None
        )

        decrypted:str = decrypted.decode('utf-8')
        return decrypted


if __name__ == "__main__":
    pass
    