#ENCAPSULATION
#PUBLIC ACCESS SPECIFIERS

class A:
    def add(self,a,b):
        self.a=a 
        self.b=b
        self.sum=a+b 
        print(self.sum) 
obj=A()
obj.add(21,81)         

#PRIVATE ACCESS SPECIFIERS
class B:
     def mul(self,a,b):
        self.__a=a 
        self.__b=b
        self.mul=a*b 
        print(self.mul) 
obj=B()
obj.mul(12,18)        

#PROTECTED ACCESS SPECIFIERS
class  C: 
      def div(self,a,b):
        self._a=a 
        self._b=b
        self.div=a/b 
        print(self.div)  

obj=C()
obj.div(45,5)         



