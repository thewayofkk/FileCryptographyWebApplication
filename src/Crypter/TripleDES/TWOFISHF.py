from twofish import Twofish
import os
from hashlib import sha512, sha256, md5
from codecs import decode
from os import urandom
from skein import skein1024
from PyPDF2 import PdfFileReader, PdfFileWriter
import random, string

#returns secure hash

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


#encrypts file via password
def fencrypt(filen, password, tweak=0, mode='twofish'):
    f=open(filen,'r')
    smstr=f.read()
    f.close()
    
    if mode=='twofish':
        if len(smstr)%16:
            nstr=str(smstr+'%'*(16-len(smstr)%16)).encode('utf-8')
        else:
            nstr=smstr.encode('utf-8')
            
        psswd=Twofish(password)
        encredstr=b'' # ENCRyptED STRing
        
        for x in range(int(len(nstr)/16)):
            encredstr+=psswd.encrypt(nstr[x*16:(x+1)*16])
            
    f=open(filen,'wb')
    f.write(encredstr)
    f.close()

    return filen

def pdfencrypt(pdFilePath, pwd):

    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(pdFilePath)
    
    for page in range(pdf_reader.getNumPages()):
        pdf_writer.addPage(pdf_reader.getPage(page))
        
        pdf_writer.encrypt(user_pwd=pwd, owner_pwd=None, use_128bit=True)
        with open(pdFilePath,"wb") as fh:
            pdf_writer.write(fh)
    
    return pdFilePath
    
    

def alphanumeric(len):
	letterNdigits = string.ascii_letters + string.digits
	result_str = ''.join((random.choice(letterNdigits) for i in range(len)))
	return result_str


def TwoMain(uploadedFile):
        
    fileOpen = "/home/kunal/Dev/src/Crypter/media/"+uploadedFile

    filepath2 , fileExtension = os.path.splitext(fileOpen)
        
    inone=alphanumeric(12)
    key_store = filepath2 + "_key"
    f = open(key_store, 'wb')
    f.write(inone.encode())
    f.close()

    #print(inone)
    if fileExtension == ".txt":
        password=gethash(inone, mode='twofish')
        encFile = fencrypt(fileOpen, password)
        return encFile, key_store
    elif fileExtension == ".pdf":
        encFile = pdfencrypt(fileOpen,inone)
        return encFile, key_store
            