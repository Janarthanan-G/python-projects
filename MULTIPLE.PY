#MULTIPLE INHERITANCE

class A:#-------->PARENT CLASS
    def add(self,a,b):
        self.a=a 
        self.b=b 
        self.sum=a+b 
        print(self.sum) 

class B: #--------->PARENT CLASS
    def mul(self,a,b): 
        self.a=a 
        self.b=b 
        self.mul=a*b 
        print(self.mul) 

class C(A,B):#-------->CHILD CLASS
    def div(self):
        self.num= self.mul/self.sum
        print("Division: {self.num}")
obj=C()
obj.mul(16,16)
obj.add(21,81) 
obj.div()                       
