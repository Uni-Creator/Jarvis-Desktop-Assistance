# importing required modules 
import subprocess as sp
import sys
from time import sleep
import PyPDF2 
import base64

# Making a list of letters to encode or decode the file this list is used later in this file and is very important
wrd_lis = [
    'q','a','z','p','l','w','s','x','o','k','m','e','d','c','i','j','n','r','f','v','u','h','b','t','g','y','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','.','?',';','"',"'",' ','@','(',':',')','%','!','#','&','*','+','[','}',']','{','=','$','\\','/','^',',','<','>','_','-','|','~'
          ]

def lisTostr(lis):
    str1 = ''
    for i in lis:
        str1 += i
    return str1
   
def pdf_read(file):
    # creating a pdf file object 
    with open(file, 'rb') as pdfFileObj:
#         creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#         printing number of pages in pdf file 
        pgnm = pdfReader.numPages
        text = ''
        for i in range(0,pgnm):
#             creating a page object 
            pageObj = pdfReader.getPage(i) 
#             extracting text from page 
            s = pageObj.extractText()
            text += s
        return text

def decoder(path,text=False):
    if not text:
        nm = path
        try:
            with open(nm) as file:
                read = file.read()
        except FileNotFoundError as e:
            return False
    else:
        read = text
    read = read.encode('ascii')
    read = base64.b64decode(read)
    read = read.decode('ascii')
    dec_lis = []
    for j in read:
        if j == '`':
            j = '\n'
            dec_lis.append(j)
        elif j in wrd_lis:
            # if j == '-':
            #     dec_lis.append(j)
            # else:
            ind2 = wrd_lis.index(j)
            j = wrd_lis[ind2-1]
            dec_lis.append(j)
        #    print(dec_lis)
    txt2 = lisTostr(dec_lis)
    return txt2

def encoder(text,path=None):
    
    if text:
        read = text
    else:
        nm = path
        if nm.endswith('.pdf'):
            read = pdf_read(nm)
        else:
            try:
                with open(nm) as file:
                    rd = file.read()
                    read = rd
            except FileNotFoundError as e:
                return False
    dec_enc_lis = []
    try:
        for r in read:
            if r == '\n':
                r = '`'
                dec_enc_lis.append(r)
            elif r == '~': # change - with esc
                    dec_enc_lis.append(r)
            else:
                if r in wrd_lis:
                    ind2 = wrd_lis.index(r)
                    r = wrd_lis[ind2+1]
                    dec_enc_lis.append(r)
#                print(dec_enc_lis)
        txt3 = lisTostr(dec_enc_lis)
        txt3 = txt3.encode('ascii')
        txt3 = base64.b64encode(txt3)
        txt3 = txt3.decode('ascii')
        return txt3
    except FileNotFoundError as e:
        return False