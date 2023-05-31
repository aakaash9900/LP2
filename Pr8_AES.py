import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

SECRET_KEY = b'123456789'
SALT_VALUE = b'abcdefg'

def encrypt(str_to_encrypt):
    iv = get_random_bytes(16)
    key = PBKDF2(SECRET_KEY, SALT_VALUE, dkLen=32, count=65536)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(str_to_encrypt.encode(), 16))
    return base64.b64encode(iv + ciphertext).decode()

def decrypt(str_to_decrypt):
    ciphertext = base64.b64decode(str_to_decrypt)
    iv = ciphertext[:16]
    key = PBKDF2(SECRET_KEY, SALT_VALUE, dkLen=32, count=65536)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext[16:]), 16).decode()
    return plaintext


# Driver code
original_val = "This is a secret message"
encrypted_val = encrypt(original_val)
decrypted_val = decrypt(encrypted_val)

print("Original value:", original_val)
print("Encrypted value:", encrypted_val)
print("Decrypted value:", decrypted_val)