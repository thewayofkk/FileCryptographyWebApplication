import zlib
import base64
from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from pathlib import Path
import os

def decrypt_blob(file_path, private_key):

    #Import the Private Key and use for decryption using PKCS1_OAEP
    privateKeyF = open(private_key, 'rb')      #import private key
    privatekey = RSA.importKey(privateKeyF.read())

    rsakey = PKCS1_OAEP.new(privatekey)

    fd = open(file_path, "rb") #open encrypted file
    encrypted_blob = fd.read()
    fd.close()

    #Base 64 decode the data
    encrypted_blob = base64.b64decode(encrypted_blob)

    chunk_size = 512
    offset = 0
    decrypted = bytearray()

    #keep loop going as long as we have chunks to decrypt
    while offset < len(encrypted_blob):
        #The chunk
        chunk = encrypted_blob[offset: offset + chunk_size]

        #Append the decrypted chunk to the overall decrypted file
        decrypted += rsakey.decrypt(chunk)

        #Increase the offset by chunk size
        offset += chunk_size

    #return the decompressed decrypted data
    fd = open(file_path, "wb")     #write unecrypted data to file 
    fd.write(zlib.decompress(decrypted))
    fd.close()
    #return zlib.decompress(decrypted)
    return file_path

def rsaDec(uploadedFile1,uploadedFile2):
    file_open = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile1
    privateKeyFile = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile2

    filepath2 , fileExtension = os.path.splitext(file_open)
    #privateKeyFile, fileExtension3 = os.path.splitext(file_open2)

    if fileExtension == '.txt':
        rsaDec = decrypt_blob(file_open, privateKeyFile)
        return rsaDec
    elif fileExtension == '.jpg' or '.jpeg':
        rsaDec = decrypt_blob(file_open, privateKeyFile)
        return rsaDec
    elif fileExtension == '.docx' or '.xls':
        rsaDec = decrypt_blob(file_open, privateKeyFile)
        return rsaDec