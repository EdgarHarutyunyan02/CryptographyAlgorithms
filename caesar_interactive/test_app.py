
from app import encrypt


def length_are_equal():
    key = 5
    original = "Hello world"
    encrypted = encrypt(original, key)
    decrypted = encrypt(encrypted, -key)
    assert len(original) == len(
        encrypted), "The length of encrypted and original texts should be equal"
    assert len(
        encrypted) == len(decrypted), "The length of encrypted and decrypted texts should be equal"


def decrypting_encrypted_text():
    key = 15
    original = "Hello world"
    encrypted = encrypt(original, key)
    decrypted = encrypt(encrypted, -key)
    assert decrypted == original, "Decryption of the encrypted text shuld result in the original text."


if __name__ == '__main__':
    length_are_equal()
    decrypting_encrypted_text()
