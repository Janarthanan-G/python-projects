#INHERITANCE
#SIMPLE INHERITANCE
class A:#----->PARENT CLASS
    def add(self,a,b):
     self.a=a
     self.b=b
     self.sum=a+b
     print(self.sum)
class B(A):#--------->CHILD CLASS
    def div(self,a,b):
        div=a/b 
        print(div)

#SIMPLE INHERITANCE
class A1:
    def __init__(self,a,b):
     self.a="MOHAN"
     self.b="MALE"
     print(self.a,self.b)
obj=A1("NAME","GENDER")
print(obj.a)
print(obj.b)

obj=B()
obj.add(12,11)
obj.div(4,6)


    

