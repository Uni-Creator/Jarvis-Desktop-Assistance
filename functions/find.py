import os

exe_list=[]

# print(os.walk("."))

for root, dirs, files in os.walk("E:\\"):
    print (dirs)
    print(root)
    print(files)
    for j in dirs:
        for i in files:
            if i.endswith('.exe'):
                # p=os.getcwd()+'/'+j+'/'+i
                p=root+'\\'+'\\'+i
                # print(p)
                exe_list.append(p)
    print()


for i in exe_list :
    print('index : {} file :{}'.format(exe_list.index(i),i.split('\\')[-1]))

ip=int(input('Enter index of file :'))

print(f'executing "{exe_list[ip]}"...')
os.system(f'"{exe_list[ip]}"')