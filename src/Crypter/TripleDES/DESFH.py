from pyDes import *
import os

# For Python3, you'll need to use bytes, i.e.:
#pyDes.triple_des(key, [mode], [IV], [pad], [padmode])
#d = k.encrypt(data)
#data = b"Please encrypt my data "
#k = triple_des(key, CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)


def encrypt_file(file_name, key_file):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()

    with open(key_file, 'rb') as foo:
        key = foo.read()
    
    foren = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    encrypted_data = foren.encrypt(plaintext)
    
    f=open(file_name,'wb')
    f.write(encrypted_data)
    f.close()

    return file_name



def encryptPDF(fileName, keyFile):
    with open(fileName, 'rb') as fo:
        plaintext = fo.read()

    with open(keyFile, 'rb') as foo:
        key = foo.read()

    foren = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    encryptedPDF_data = foren.encrypt(plaintext)

    f=open(fileName,'wb')
    f.write(encryptedPDF_data)
    f.close

    return fileName



def encryptIMG(fileImgName, keyImgFile):
    with open(fileImgName, 'rb') as fo:
        plaintext = fo.read()

    with open(keyImgFile, 'rb') as foo:
        key = foo.read()

    forenc = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    encryptIMG_data = forenc.encrypt(plaintext)

    f=open(fileImgName, 'wb')
    f.write(encryptIMG_data)
    f.close

    return fileImgName

def encryptOfficeFile(fileOfcName, keyOfcFile):
    with open(fileOfcName, 'rb') as fo:
        plaintext = fo.read()

    with open(keyOfcFile, 'rb') as foo:
        key = foo.read()

    ofcenc = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    encryptOfc_data = ofcenc.encrypt(plaintext)

    f = open(fileOfcName, 'wb')
    f.write(encryptOfc_data)
    f.close()

    return fileOfcName


def mainProg(uploaded_file):
    file_open = "/home/kunal/Dev/src/Crypter/media/"+uploaded_file
    filepath2 , fileExtension = os.path.splitext(file_open)
    
    key = os.urandom(24)
    key_store = filepath2 + "_key"
    f = open(key_store,'wb')
    f.write(key)
    f.close()
    
    if fileExtension == ".txt":
        enc_file = encrypt_file(file_open, key_store)
        return enc_file, key_store
    elif fileExtension == ".pdf":
        enc_file = encryptPDF(file_open, key_store)
        return enc_file, key_store
    elif fileExtension == ".jpg" or ".jpeg" or ".png":
        enc_file = encryptIMG(file_open, key_store)
        return enc_file, key_store
    elif fileExtension == ".docx" or ".xls":
        enc_file = encryptOfficeFile(file_open,key_store)
        return enc_file, key_store



