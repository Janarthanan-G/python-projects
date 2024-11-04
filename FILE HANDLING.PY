#EXCEPTION HANDLING
try:
    f.open('file.txt','x') #To create file with the mode of 'x'-->denoded as create
except:
    print("The file is created already by the programmer")   
#FILE HANDLING     
f=open('file.txt','w') # To write function with mode of 'w'-->denoded as write
f.write('This is my python program')
f.close()
f=open('file.txt','a') #To add the elements at the end with mode of 'a'-->denoded as append
f.write('where I learn')
f.close()
f=open('file.txt','r') #To read the file with mode of 'r'-->denoded as read
print(f.read())
f=open('file.txt','w')#To overwrite the function with mode of 'w'-->denoded as write
f.write('I am a DATA SCIENCE student')
f.close()
import os
if os.path.exists('file.txt'):
    os.remove('file.txt')
else:
    print('The file does not created by programmer')    