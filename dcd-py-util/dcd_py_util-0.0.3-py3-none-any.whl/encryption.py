import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

PHRASE_SIZE = 64
SALT_SIZE = 16
KEY_SIZE = [32, 60]

ENCODING = 'utf-8'

ENCRYPTED_LABEL = "Encrypted "


def scramble(encrypted_message: str) -> str:
    _result = encrypted_message[0:2]
    for i in range(2, len(encrypted_message) - 2, 2):
        _result += encrypted_message[(i + 1):(i + 2)] + \
                   encrypted_message[i:(i + 1)]
    _result += encrypted_message[-2:]
    return _result


def encrypt(plain_text: str) -> str:
    _phrase = os.urandom(PHRASE_SIZE)
    _salt = os.urandom(SALT_SIZE)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_SIZE[0],
        salt=_salt,
        iterations=480000,
    )
    _key = base64.urlsafe_b64encode(kdf.derive(_phrase))
    _f = Fernet(_key)
    _encrypted_text = _f.encrypt(plain_text.encode(ENCODING))
    _result_key = base64.urlsafe_b64encode(_key).decode(ENCODING)
    _result_encrypted = base64.urlsafe_b64encode(_encrypted_text).decode(ENCODING)
    _result = _result_key + _result_encrypted
    return scramble(_result)


def decrypt(scrambled_message: str) -> str:
    if scrambled_message.startswith(ENCRYPTED_LABEL):
        scrambled_message = scrambled_message.replace(ENCRYPTED_LABEL, "")
    _encrypted_message = scramble(scrambled_message)
    _key = base64.b64decode(bytes(_encrypted_message[0:KEY_SIZE[1]], ENCODING))
    _encrypted = base64.b64decode(bytes(_encrypted_message[KEY_SIZE[1]:], ENCODING))
    _f = Fernet(_key)
    _result = _f.decrypt(_encrypted).decode(ENCODING)
    return _result


def encrypt_with_label(plain_text: str) -> str:
    _scrambled_message = "{}{}".format(ENCRYPTED_LABEL, encrypt(plain_text))
    return _scrambled_message
