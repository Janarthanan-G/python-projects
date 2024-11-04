#HIERARICAL INHERITANCE
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
                  
                