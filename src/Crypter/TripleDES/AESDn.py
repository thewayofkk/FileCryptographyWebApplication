from Crypto import Random
from Crypto.Cipher import AES
import os

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()

    with open(key,'rb') as keyy:
        encryption_key = keyy.read()
    
    dec = decrypt(ciphertext, encryption_key)
    with open(file_name, 'wb') as fo:
        fo.write(dec)
    
    return file_name


#key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
#key = b'\xd9x\x8c\xd1Y\xa9\xb9\x11S\xed\xdc\x10\x8ex\xca7\xc0\xcd0c\xf9!>\xef\x17\xec\xa0\t\xc4T\xaa\xdb\xdf\x98'

def decMain(uploadedFile1, uploadedFile2):
        
    file_open = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile1
    filepath2 , fileExtension = os.path.splitext(file_open)
    keyFile = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile2

    if fileExtension == ".txt":
        decFile = decrypt_file(file_open,keyFile)
        return decFile
    elif fileExtension == '.jpg' or '.jpeg':
        decFile = decrypt_file(file_open, keyFile)
        return decFile
    elif fileExtension == '.docx' or '.xls':
        decFile = decrypt_file(file_open, keyFile)
        return decFile