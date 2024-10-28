# importing required modules 
import subprocess as sp
import sys
from time import sleep
import PyPDF2 
from colored import fg, bg, attr
from colored import fore, back, style
import base64


wrd_lis = [
    'q','a','z','p','l','w','s','x','o','k','m','e','d','c','i','j','n','r','f','v','u','h','b','t','g','y','Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M','1','2','3','4','5','6','7','8','9','0','.','?',';','"',"'",' ','@','(',':',')','%','!','#','&','*','+','[','}',']','{','=','$','\\','/','^',',','<','>','_','-','|','~'
          ]
# change wrd_lis[-1] with esc

def progress(text):
    print('')
    f = ['#         ','##        ','###       ','####      ','#####     ','######    ','#######   ','########  ','######### ','##########']
    for i in f:
        sys.stdout.write(f"\r{fg('white')}{bg('yellow')} {text} [{i}] {attr('reset')}")
        sys.stdout.flush()
        sleep(0.10)
    print('')

def lisTostr(lis):
    str1 = ''
    for i in lis:
        str1 += i
    return str1
#print(lisTostr(wrd_lis))

def cmd():
    while True:
        print (fg(15) + ' [1] Decode a file \n [2] Create a new file \n [3] Encode a file \n [4] Exit \n' + attr('reset'))

        ask = input(fg(2) +'Enter Your choices : ' + fg(15))

        if ask.isnumeric():
            ask = int(ask)
            if ask<=0:
                sp.run('cls',shell=True)
                print(f'{fg(1)}\nWrong input...\n{attr(0)}')
            elif ask>=5:
                sp.run('cls',shell=True)
                print(f'{fg(1)}\nWrong input...\n{attr(0)}')
            else:
                return ask
        else:
                sp.run('cls',shell=True)
                print(f'{fg(1)}\nWrong input...\n{attr(0)}')
    
def pdf_read(file):
    # creating a pdf file object 
    with open(file, 'rb') as pdfFileObj:
#         creating a pdf reader object 
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
#         printing number of pages in pdf file 
        pgnm = pdfReader.numPages
        lis = []
        x = pgnm - 1
        while True:
            if x == 0:
                lis.append(x)
                break
            lis.append(x)
            x -= 1
        text = ''
        for i in lis:
#             creating a page object 
            pageObj = pdfReader.getPage(i) 
#             extracting text from page 
            s = pageObj.extractText()
            text += s
        return text


sp.run('cls',shell=True)
while True:
    ask = cmd()
    sp.run('cls',shell=True)
    if ask == 1:
        nm = input(fg(3) + "\nEnter the file path with name : " + fg(15))
        print('')
        try:
            with open(nm) as file:
                read = file.read()
                read = read.encode('ascii')
                read = base64.b64decode(read)
                read = read.decode('ascii')
                dec_lis = []
                for j in read:
                    if j == '`':
                        j = '\n'
                        dec_lis.append(j)
                    elif j in wrd_lis:
#                        if j == '-':
#                            dec_lis.append(j)
#                        else:
                        ind2 = wrd_lis.index(j)
                        j = wrd_lis[ind2-1]
                        dec_lis.append(j)
                dec_lis1 = []
                for j in lisTostr(dec_lis):
                    if j == '`':
                        j = '\n'
                        dec_lis1.append(j)
                    elif j in wrd_lis:
#                        if j == '-':
#                            dec_lis.append(j)
#                        else:
                        ind2 = wrd_lis.index(j)
                        j = wrd_lis[ind2-1]
                        dec_lis1.append(j)
#                print(dec_lis)
                txt2 = lisTostr(dec_lis)
                print(txt2)
                input('')
        except FileNotFoundError as e:
            print(f'{fg(1)}{e}\n{attr(0)}')
            input('')

    elif ask == 2:
        nm = input(fg(3) + "\nEnter the file path with name : " + fg(15))
        print (fore.LIGHT_BLUE + back.RED + style.BOLD + '\nInstruction:\n1.Press Enter to save the file.\n2.For newline type +.\n' + style.RESET)
        cho = input(''+ fg(15))
        enc_lis = []
        for i in cho:
            if i in wrd_lis:
                if i == '`':
                    enc_lis.append(i)
                elif i == '~': # change - with esc
                    enc_lis.append(i)
                else:
                    ind = wrd_lis.index(i)
                    i = wrd_lis[ind+1]
                    enc_lis.append(i)
#        print(enc_lis)
        txt = lisTostr(enc_lis)
        txt = txt.encode('ascii')
        txt = base64.b64encode(txt)
        txt = txt.decode('ascii')
#        print(txt)
        try:
            with open(f'{nm}','+w') as file:
                file.write(txt)
            print('\n\tFile(s) saved...')
            input('')
        except FileNotFoundError as e:
            print(f'{fg(1)}{e}\n{attr(0)}')
            input('')
    elif ask == 3:
        nm = input(fg(3) + "\nEnter the file path with name : " + fg(15))
        if nm.endswith('.pdf'):
            read = pdf_read(nm)
        else:
            try:
                with open(nm) as file:
                    rd = file.read()
                    read = rd
            except FileNotFoundError as e:
                print(f'\n{fg(1)}{e}\n{attr(0)}')
                input('')
                sp.run('cls',shell=True)
                continue
        dec_enc_lis = []
        progress('Encoding the file')
        try:
            for r in read:
                # dec_enc_lis.append(r)
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
#                print(txt3)
            with open(f'{nm}','w') as file:
                file.write(txt3)
            print(f'\n\t\tFile saved as {nm}')
            input('')
        except FileNotFoundError as e:
            print(f'{fg(1)}{e}\n{attr(0)}')
            input('')
    elif ask == 4:
        input(f"{fg('orchid')}{attr('bold')} Logout \n Process completed with code [127] - Press Enter{attr('reset')} ")
        exit('')
    sp.run('cls',shell=True)