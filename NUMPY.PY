#COPY AND VIEWS :
a=[2.5,'PYTHON',22,True,'C++',88j]
x=a.copy()
print(x)
a[0]=10
print(a)
print(x)

a1=[-2.3,-4j,-67,'Java',True,35]
x=a1[:]
print(x)
a1[0]=10
print(x)
print(a1)

#RESHAPE AND JOIN:
import numpy
a=numpy.array([1,2,3,4,5,6,7,8,9,10])
newarr=a.reshape(10,1)
print(newarr)

a1=numpy.array([1,2,3,3.5])
a2=numpy.array([3.5,4,5,6])
a=numpy.concatenate((a1,a2))
print(a)



