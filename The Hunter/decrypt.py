from base64 import b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def decrypt(encrypted):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = unpad(cipher.decrypt(b64decode(encrypted)), AES.block_size)
    return decrypted.decode('utf-8')


key = b'aa0d28c82a0a491bc6ba4883a2e85d29'
iv = b'8497d52c9bde1689'
encrypted = "Z5dTXFyUTK9F5+Y9lDl0UdVyL63sDbN2ePDajnLXoXLbdfR5w6tCrGfGcmNslX18sJV2g8E42q8rhzt2DeYrfjQrP145eGYWy/vTruslc08="

api = decrypt(encrypted)
print(f"key = {api}")
