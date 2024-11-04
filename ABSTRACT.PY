#ABSTRACT CLASS
from abc import ABC, abstractmethod
class pentagon(ABC):
    @abstractmethod
    def sides(self):
        pass

class triangle(pentagon):
    def sides(self):
        
        print("triangle")

class rectangle(pentagon):
    def sides(self):
        
        print("rectangle")   

objt=triangle()
objr=rectangle()  
objt.sides()
objr.sides()           