#TYPES OF MODULES
#USER DEFINED MODULES
import PACKAGE1
print(PACKAGE1.d['Name'])
print(PACKAGE1.d['Mail'])
print(PACKAGE1.S)
print(PACKAGE1.L)

#BUILD-IN MODULES
import math#------->example-1
a=math.sqrt(5)
b=math.pow(5,10)
print(a,b)

from math import sqrt, factorial  #------->example-2
print(sqrt(25))
print(factorial(7))

from math import factorial #------->example-3
print(factorial(55))


