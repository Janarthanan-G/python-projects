#list comprehension
for i in range(10):
    print(i,end=" ")
print() 
L=[21,12,18,"PYTHON",True,0.001,20]
for i in L:
    print(i,end=" ")
print() 

#lambda functions
x=lambda a,b,c:a-b*c
print(x(2,7,11))
y=lambda a,b,c,d:a+b*c/d
print(y(12,18,20,1))
x1=lambda a,b,c,d,e:a%b+c-d*e
print(x1(18,12,4,33,7))

#Reverse the number
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers.reverse()
print(numbers)

#inheritance
class A:
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender

class B(A):
    def __init__(self,company,id,name,gender):
        super().__init__(id,name,gender)
        self.company=company

class C(A): 
     def __init__(self,role,id,name,gender):   
         super().__init__(id,name,gender)
         self.role=role

     def print_data(self):    
         print("EMPLOYEE ID IS:",self.id)
         print("EMPLOYEE NMAE IS:",self.name)
         print("EMPLOYEE GENDER IS:",self.gender) 
         print("EMPLOYEE ROLE IS:",self.role) 

obj =C("DATA SCIENCE",25021,"KRISHNA" ,"MALE")   
obj.print_data() 


#exception handling
def division(a,b):
    try:
        result=b/a
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
division(20,100) 

#file handling
try:
    f.open('file.txt','x') #To create file with the mode of 'x'-->denoded as create
except:
    print("The file is created already by the programmer")        
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


#capitalize the sentence
txt = "i complete my ug degree in the college of kumaraguru."
A= txt.title()
print (A)


#palindrome, Armstrong
