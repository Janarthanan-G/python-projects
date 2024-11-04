#numpy--array:
import numpy
arr=numpy.array([1,2,3])
print(arr)
print(arr[0])
print(arr[0]+arr[2])
print(type(arr))

#2D ARRAY AND SLICING :
import numpy
arr=numpy.array([[0.2,1.3,6.6],[5,6,10]])
print(arr)
print(arr[1][2])
print(arr[0][0])
print(arr[0:2,1])
arr=numpy.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[0:2,1:4])

#3D ARRAY AND SLICING :
import numpy
arr=numpy.array([[[1,2,3,4,5],[3.3,2.01,7,27,22],[0.001,2,8,11,707]]])
print(arr)
print(arr[0,1,1])
print(arr[0,0,2])
print(arr[1:2,2:4])

#ARRAY USING STRING :
import numpy
arr=numpy.array(['JAVA','PYTHON','C++','PHP','R'])
print(arr)
print(arr[0])
print(type(arr))

import numpy
arr=numpy.array(['A',22,0.75,True,5j,'PYTHON'])
print(arr)
print(arr[4])
print(type(arr))