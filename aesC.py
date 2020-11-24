from Crypto.Cipher import AES
import base64
from Crypto.Random import random
import binascii

def cifrarAes(cadena,key):

    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(cadena)
    return (ciphertext,nonce,tag)

def descifrarAes(cadena,noncee,key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=noncee)
    plaintext = cipher.decrypt(cadena)
    return(plaintext)
if __name__ == "__main__":
    key = b'Sixteen byte key'
    cadena = (b'https://www.saes.upiicsa.ipn.mx/')
    ciphertext,nonce,tag = cifrarAes(cadena,key)
    descifrado = descifrarAes(ciphertext,nonce,key)
    print(descifrado)