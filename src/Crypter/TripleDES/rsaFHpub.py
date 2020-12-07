import zlib
import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path
import os

def generate_keys():
	# RSA modulus length must be a multiple of 256 and >= 1024
	modulus_length = 4096 # use larger value in production
	privatekey = RSA.generate(modulus_length, Random.new().read)
	publickey = privatekey.publickey()
	return privatekey, publickey


def encrypt_blob(file_path, public_key):
    
    publicKeyFile = open(public_key, 'rb')
    publickey = RSA.importKey(publicKeyFile.read())


    fd = open(file_path, "rb")
    blob = fd.read()
    fd.close()

    rsa_key = PKCS1_OAEP.new(publickey)

    #compress the data first
    blob = zlib.compress(blob)
    chunk_size = 470
    offset = 0
    end_loop = False
    encrypted = bytearray()

    while not end_loop:
        #The chunk
        chunk = blob[offset:offset + chunk_size]

        if len(chunk) % chunk_size != 0:
            end_loop = True
            #chunk += b" " * (chunk_size - len(chunk))
            chunk += bytes(chunk_size - len(chunk))
        encrypted += rsa_key.encrypt(chunk)

        offset += chunk_size

    #Base 64 encode the encrypted file
    fd = open(file_path, "wb")
    fd.write(base64.b64encode(encrypted))
    fd.close()
    #return base64.b64encode(encrypted)
    return file_path


def mainRSA(enc_file):
    file_open = "/home/kunal/Dev/src/Crypter/media/"+enc_file
    filepath2 , fileExtension = os.path.splitext(file_open)
    
    privatekey , publickey = generate_keys() #generated Keys

    privateKeyFile = filepath2 + "_priv_key"        #writing both keys in file
    f = open(privateKeyFile, 'wb')
    f.write(privatekey.exportKey('PEM'))
    f.close()

    publicKeyFile = filepath2 + "_pub_key"
    f2 = open(publicKeyFile, 'wb')
    f2.write(publickey.exportKey('PEM'))
    f2.close()


    if fileExtension == '.txt':
        encFile = encrypt_blob(file_open, publicKeyFile)
        return encFile, publicKeyFile, privateKeyFile
    elif fileExtension == '.jpg' or '.jpeg':
        encFile = encrypt_blob(file_open, publicKeyFile)
        return encFile, publicKeyFile, privateKeyFile
    elif fileExtension == '.docx' or '.xls':
        encFile = encrypt_blob(file_open, publicKeyFile)
        return encFile, publicKeyFile, privateKeyFile