

 

import base64
from Crypto.Cipher import AES
import time
key=input("密码是什么:")
text=input("要解密什么:")
def add_to_32(value):
    while len(value)%32!=0:
        value=value+b'\x00'
    return value
def decrypt_oralce():
    aes = AES.new(add_to_32(key), AES.MODE_ECB)
    base64_decrypted = base64.decodebytes(text.encode())
    decrypted_text = str(aes.decrypt(base64_decrypted),encoding='utf-8').replace('\x00','') 
    print(decrypted_text)
key=key.encode()
key=add_to_32(key)
if len(key)>32:
    key=key[:32]
decrypt_oralce()
time.sleep(100)
