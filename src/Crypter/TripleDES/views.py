from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper
from TripleDES.DESFH import mainProg
from TripleDES.DESSH import mainDecDES
from TripleDES.rsaFHpub import mainRSA
from TripleDES.rsaSHpri import rsaDec
from TripleDES.TWOFISHF import TwoMain
from TripleDES.TWOFISHS import decTWOMain
from TripleDES.AESEn import aesMain
from TripleDES.AESDn import decMain
import os


def home_page(request):
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,"index.html")

enc_file = ""
key_file = ""
fname = ""
kname = ""
def blanktrides(request):
    return render(request,"DES3.html")

def trides(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        final_file = fs.save(uploaded_file.name,uploaded_file)
        global enc_file,key_file
        global fname,kname
        enc_file, key_file  = mainProg(final_file)
        dirname, fname = os.path.split(enc_file)
        dirname2, kname = os.path.split(key_file)
        #print(fname)
        #print(kname)
        #return render(request,"DES3.html",{"enc_file":enc_file,"key_file":key_file})
    return render(request,"DES3En.html",{"fname":fname,"kname":kname})

dec_file = ""
decDES = ""
def tridesDec(request):
    if request.method == 'POST':
        uploaded_file1 = request.FILES['document1']
        uploaded_file2 = request.FILES['document2']
        #print(uploaded_file1)
        #print(uploaded_file2)
        fs = FileSystemStorage()
        fs1 = FileSystemStorage()
        final_file1 = fs.save(uploaded_file1.name,uploaded_file1)
        final_file2 = fs1.save(uploaded_file2.name,uploaded_file2)
        global dec_file,decDES
        dec_file = mainDecDES(final_file1,final_file2)
        dirname, decDES = os.path.split(dec_file)
    return render(request,"DES3Dn.html",{"decDES":decDES})

def blankrsa(request):
    return render(request,"RSA.html")

enc_rsa = ""
enc_pub = ""
enc_pri = ""
frsa = ""
kpubrsa = ""
kprirsa = ""
def RSA(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        finalFile = fs.save(uploaded_file.name,uploaded_file)
        global enc_pri,enc_pub,enc_rsa
        global frsa, kpubrsa, kprirsa
        enc_rsa, enc_pub, enc_pri = mainRSA(finalFile)

        dirname, frsa = os.path.split(enc_rsa)
        dirname2, kpubrsa = os.path.split(enc_pub)
        dirname3, kprirsa = os.path.split(enc_pri)

    return render(request,"RSAEn.html",{"frsa":frsa,"kpubrsa":kpubrsa,"kprirsa":kprirsa})

decRSA = ""
def RSADec(request):
    if request.method == 'POST':
        uploaded_file1 = request.FILES['document1']
        uploaded_file2 = request.FILES['document2']

        fs = FileSystemStorage()
        fs1 = FileSystemStorage()

        final_file1 = fs.save(uploaded_file1.name,uploaded_file1)
        final_file2 = fs1.save(uploaded_file2.name,uploaded_file2)

        global decRSA
        decRSAfile = rsaDec(final_file1,final_file2)
        dirname, decRSA = os.path.split(decRSAfile)

    return render(request,"RSADn.html",{"decRSA":decRSA})

def blanktwofish(request):
    return render(request,"TWOFISH.html")

encTWO = ""
keyTWO = ""
encTWOF = ""
keyTWOF = ""
def TWOFISH(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        finalFile = fs.save(uploaded_file.name,uploaded_file)

        global encTWO, keyTWO, encTWOF, keyTWOF
        encTWO, keyTWO = TwoMain(finalFile)

        dirname, encTWOF = os.path.split(encTWO)
        dirname2, keyTWOF = os.path.split(keyTWO)

    return render(request,"TWOFISHEn.html",{"encTWOF":encTWOF,"keyTWOF":keyTWOF})

decTWO = ""
def TWOFISHDec(request):
    if request.method == 'POST':
        uploaded_file1 = request.FILES['document1']
        uploaded_file2 = request.FILES['document2']

        fs = FileSystemStorage()
        fs1 = FileSystemStorage()

        final_file1 = fs.save(uploaded_file1.name,uploaded_file1)
        final_file2 = fs1.save(uploaded_file2.name,uploaded_file2)

        global decTWO
        decTWOFile = decTWOMain(final_file1, final_file2)
        dirname, decTWO = os.path.split(decTWOFile)

    return render(request,"TWOFISHDn.html",{"decTWO":decTWO})

def blankAES(request):
    return render(request,"AES.html")

encAES = ""
keyAES = ""
encAESF = ""
keyAESF = ""
def AES(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        finalFile = fs.save(uploaded_file.name,uploaded_file)

        global encAES, keyAES, encAESF, keyAESF
        encAES, keyAES = aesMain(finalFile)

        dirname, encAESF = os.path.split(encAES)
        dirname2, keyAESF = os.path.split(keyAES)
    return render(request,"AESEn.html",{"encAES":encAESF,"keyAES":keyAESF})

decAES = ""
def AESDec(request):
    if request.method == 'POST':
        uploaded_file1 = request.FILES['document1']
        uploaded_file2 = request.FILES['document2']

        fs = FileSystemStorage()
        fs1 = FileSystemStorage()

        final_file1 = fs.save(uploaded_file1.name,uploaded_file1)
        final_file2 = fs1.save(uploaded_file2.name,uploaded_file2)

        global decAES
        decAESFile = decMain(final_file1, final_file2)
        dirname, decAES = os.path.split(decAESFile)
    
    return render(request,"AESDn.html",{"decAES":decAES})

def aboutus(request):
    return render(request,"aboutus.html")