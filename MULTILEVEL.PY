#MULTILEVEL INHERITANCE
class A:
    def __init__(self,name,age,course):
        self.name=name
        self.age=age
        self.course=course
       

class B(A):
    def __init__(self,phone,name,age,course): 
        super().__init__(name,age,course)
        self.phone = phone 

class C(B):
    def __init__(self,phone,name,age,course): 
        super().__init__(phone,name,age,course)
    def print_data(self):
        print("HIS/HER NAME IS:",self.name)
        print("HIS/HER AGE IS:",self.age)   
        print("HIS/HER COURSE IS:",self.course)   
        print("HIS/HER PHONE IS:",self.phone)  

obj = C(1234567890, "KRISHNA", 21, "DATA SCIENCE")   
obj.print_data()                    
         