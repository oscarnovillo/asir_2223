import binascii
import hashlib
import random
import secrets
import string


class PasswordHash:
    __NUM_ITERACCIONES = 1000
    __HASH_LENGTH = 24
    __SALT_LENGTH = 24

    def checkPassword(self, password, hashPassword):
        camposPassword = hashPassword.rsplit(':')
        key = hashlib.pbkdf2_hmac('sha256', bytearray(password, 'UTF-8'), \
                                  binascii.unhexlify(camposPassword[1]), int(camposPassword[0]),
                                  dklen=self.__HASH_LENGTH)
        return key.__eq__(binascii.unhexlify(camposPassword[2]))

    def hashPassword(self, password):
        salt = secrets.token_bytes(self.__SALT_LENGTH)
        key = hashlib.pbkdf2_hmac('sha256', bytearray(password, 'UTF-8'), \
                                  salt, self.__NUM_ITERACCIONES, dklen=self.__HASH_LENGTH)
        return str(self.__NUM_ITERACCIONES) + ":" + salt.hex() + ":" + key.hex()


def get_random_alphaNumeric_string(length=8):
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join((random.choice(lettersAndDigits) for i in range(length)))

