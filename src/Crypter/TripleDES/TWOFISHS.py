from twofish import Twofish
from hashlib import sha512, sha256, md5
from codecs import decode
from pathlib import Path
import os
from os import urandom
from skein import skein1024
from PyPDF2 import PdfFileReader, PdfFileWriter


def gethash(smstr, mode='twofish'):
	#generating salt
	salt=b'gierghyuihflfugirugh89GYOB  IIUH ^%^&& YHGVF!@#$**R F MV GV^I"OLp;of\e\3 t49hrhf h hrushg vb'
	nhash=skein1024(salt+smstr.encode('ascii')).digest()
	tweak=salt+smstr.encode('ascii')

	# generating key 2^18 times
	if mode=='twofish':
		for x in range(2**18):
			nhash=sha512(salt+nhash).digest()
		return sha256(salt+nhash).digest()


def fdecrypt(filen, password, tweak=0, mode='twofish'):
    f=open(filen,'rb')
    smstr=f.read()
    f.close()
    
    if mode=='twofish':
        psswd=Twofish(password)
        decredstr=b''
        # decrypting blocks
        for x in range(int(len(smstr)/16)):
            decredstr+=psswd.decrypt(smstr[x*16:(x+1)*16])
    
    final = decode(decredstr,'utf-8')
    f=open(filen,'w')

    for i in range(0,len(final)):
        if final[i] == "%":
            f.close()
        else:
            f.write(final[i])
    f.close()

    return filen
    #return decode(decredstr,'utf-8').strdnip('%')


def pdfdecrypt(pdfPath, passwd):
    #print(pdfPath,passwd)
    base=os.path.basename(pdfPath)
    outPath = "/home/kunal/Dev/src/Crypter/media/dec_"+base

    with open(pdfPath,'rb') as input_file, open(outPath,'wb') as output_file:
        reader = PdfFileReader(pdfPath)
        reader.decrypt(passwd)

        writer = PdfFileWriter()

        for i in range(reader.getNumPages()):
            writer.addPage(reader.getPage(i))

        writer.write(output_file)
    
    return outPath



def decTWOMain(uploadedFile1, uploadedFile2):

    filePath = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile1
        
    filepath2 , fileExtension = os.path.splitext(filePath)
    #inone=input("Password to decrypt file: ")
    key_store = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile2
    f = open(key_store, 'rb')
    inone = f.read().decode()
    f.close()
        
    if fileExtension == ".txt":
        password=gethash(inone, mode='twofish')
        decFile = fdecrypt(filePath, password)
        return decFile
    elif fileExtension == ".pdf":
        decFile = pdfdecrypt(filePath,inone)
        return decFile
    