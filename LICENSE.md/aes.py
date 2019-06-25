import base64
from Crypto.Cipher import AES
import time
def add_to_32(value):
    while len(value)%32!=0:
        value=value+b'\x00'
    return value
def encrypt_oracle():
    aes = AES.new(add_to_32(key), AES.MODE_ECB)
    encrypt_aes = aes.encrypt(add_to_32(text.encode()))
    encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8') 
    print(encrypted_text)
text=input("请输入要加密的文本:")
key=input("请输入密码:")

key=key.encode()
key=add_to_32(key)
if len(key)>32:
    key=key[:32]
encrypt_oracle()
time.sleep(100)
