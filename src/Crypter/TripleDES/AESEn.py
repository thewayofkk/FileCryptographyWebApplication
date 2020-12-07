from Crypto import Random
from Crypto.Cipher import AES
import os

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    with open(key,'rb') as keyy:
        encryption_key = keyy.read()
    enc = encrypt(plaintext, encryption_key)
    with open(file_name, 'wb') as fo:
        fo.write(enc)
    
    return file_name

def aesMain(uploadedFile):

    #key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
    file_open = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile
    filepath2 , fileExtension = os.path.splitext(file_open)
    KeyFile = filepath2 + "_key" 
    key = os.urandom(32)
    fd = open(KeyFile, "wb")
    fd.write(key)
    fd.close()
    #print(key)

    if fileExtension == ".txt":
        encFile = encrypt_file(file_open,KeyFile)
        return encFile, KeyFile
    elif fileExtension == '.jpg' or '.jpeg':
        encFile = encrypt_file(file_open, KeyFile)
        return encFile, KeyFile
    elif fileExtension == '.docx' or '.xls':
        encFile = encrypt_file(file_open, KeyFile)
        return encFile, KeyFile
    #encrypt_file('/home/kunal/TYMCA/NIS Project/DES3/testfile.txt', key)