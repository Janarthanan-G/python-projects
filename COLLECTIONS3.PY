#USERDICT COLLECTIONS:
from collections import UserDict
class Mydict(UserDict):
    def __del__(self):
        raise RuntimeError("Deletion not allowed")
    def popitem(self,s=None):
        raise RuntimeError("Deletion popitem not allowed")
    def pop(self,s=None):
        raise RuntimeError("Deletion pop not allowed")
L=Mydict({1:'a',2:'b',3:'c',4:'d'})
#L.popitem()  

#USERSTRING COLLECTIONS:
from collections import UserString
class Mystring(UserString):
    def append(self,s):
        self.data +=s
    def remove(self,s):
        self.data=self.data.replace(s,"")

s1=Mystring('python')
s1.append("ion")
print(s1)
s1.remove('y')
print(s1)           