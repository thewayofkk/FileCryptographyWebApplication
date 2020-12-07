from pyDes import *
import os


def decrypt_file(file_name, key_file):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
        
    with open(key_file, 'rb') as foo:
        key = foo.read()

    fordec = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    decrypted_data = fordec.decrypt(ciphertext)
    
    f=open(file_name,'wb')
    f.write(decrypted_data)
    f.close()

    return file_name


def decryptPDF(fileName, keyFile):
    with open(fileName, 'rb') as fo:
        ciphertext = fo.read()
    
    with open(keyFile, 'rb') as foo:
        key = foo.read()
    
    fordec = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    decryptedPDF_data = fordec.decrypt(ciphertext)

    f=open(fileName,'wb')
    f.write(decryptedPDF_data)
    f.close

    return fileName


def decryptIMG(imgFile, keyFile):
    with open(imgFile, 'rb') as imgfo:
        ciphertext = imgfo.read()
    
    with open(keyFile, 'rb') as imgfoo:
        key = imgfoo.read()

    fordecr = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    decryptedIMG_data = fordecr.decrypt(ciphertext)

    f=open(imgFile,'wb')
    f.write(decryptedIMG_data)
    f.close

    return imgFile

def decryptOfcFile(fileOfcName, keyOfcFile):
    with open(fileOfcName, 'rb') as docfo:
        ciphertext = docfo.read()

    with open(keyOfcFile, 'rb') as docfoo:
        key = docfoo.read()

    ofcdec = triple_des(key, CBC, b'E\x93\xe2\xd8\xb5\xaf4\n', pad=None, padmode=PAD_PKCS5)

    decryptedOFC_data = ofcdec.decrypt(ciphertext)

    f=open(fileOfcName,'wb')
    f.write(decryptedOFC_data)
    f.close()

    return fileOfcName

def mainDecDES(uploaded_file1,uploaded_file2):
    file_open = "/home/kunal/Dev/src/Crypter/media/"+uploaded_file1
    key_store = "/home/kunal/Dev/src/Crypter/media/"+uploaded_file2

    filepath2 , fileExtension = os.path.splitext(file_open)
    #key_store , fileExtension3 = os.path.splitext(file_open2)


    if fileExtension == ".txt":
        dec_file = decrypt_file(file_open, key_store)
        return dec_file
    elif fileExtension == ".pdf":
        dec_file = decryptPDF(file_open, key_store)
        return dec_file
    elif fileExtension == ".jpg" or ".jpeg" or ".png":
        dec_file = decryptIMG(file_open, key_store)
        return dec_file
    elif fileExtension == ".docx" or ".xls":
        dec_file = decryptOfcFile(file_open, key_store)
        return dec_file