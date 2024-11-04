#RANDOM :
import numpy
from numpy import random
x=random.randint(100,size=(20))
print(x)

#RANDOM CHOICE :
x=random.choice([1,0,0,1])
print(x)
x=random.choice([1,0,0,1],size=(3,4)) 
print(x)

#DISTRIBUTION : 
x=random.choice(['SANJAY',2.574,8.456j,'JANA','VIGNESH',77],p=[0.1,0.2,0.3,0.2,0.1,0.1],size=(210))
print(x)

#SHUFFLE :
arr=numpy.array([-2.23,-6j,0.11,'Java',False,77,'J'])
random.shuffle(arr)
print(arr)

#PERMUTATION : 
print(random.permutation(arr))
print(arr)


