#POLYMARPHISM

class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("I AM",self.name ,"MY AGE IS", self.age ,"years.")
class B:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("HIS NAME",self.name,  "HIS AGE IS ",self.age ,"years.")


    
obj1=A("SAM",20)
obj2=B("RAJA",21)
for person in (obj1,obj2):
    person.info()