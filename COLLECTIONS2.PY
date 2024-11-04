#NAMEDTUPLE COLLECTIONS:
from collections import namedtuple
from typing import Iterable
Student = namedtuple('Student', ['Name', 'Age', 'DOB','Phone_no','Mail_ID'])
S=Student('Krishna','21','18/09/2003','0123456789','krishna@gmail.com')
print("The Student name is : ", end="")
print(S.Name)
print("The Student age using is : ", end="")
print(S[1])
print("The Student phone no is : ", end="")
print(S.Phone_no)
print("The Student Mail is : ", end="")
print(S.Mail_ID)

#ORDERED COLLECTIONS:
from collections import OrderedDict
d= OrderedDict()
d['Student name is']='Mohan'
d['College name is']='Kumaraguru College of Technology'
d['Department of']='Electronics and Communiocation Engineering'
d['Year of passing']='2024'
for key, value in d.items():
    print(key, value)
    
#USERLIST COLLECTIONS:
from collections import UserList
class mylist(UserList):
    def append(self,s=None):
        raise RuntimeError("Insertion not allowed")
    def extend(self, s=None):
        raise RuntimeError("Insertion not allowed")
    def insert(self,s=None):
        raise RuntimeError("Insertion not allowed")
l=mylist([1,2,3])
l.append(3)
l.insert(2)    


