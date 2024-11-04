#COLLECTION MODULES
#DEQUE MODULES
from collections import deque
de=deque([21,12,42,57,20,"Java",True,4j,5.5])
de.appendleft(30)
print(de)
de.extendleft([12,56,5,8,99,47,8j,201])
print(de)
de.pop()
print(de)
de.popleft()
print(de)
#CHAIN-MAP MODULES
from collections import ChainMap
d1={1:'a',2:'c',3:'b'} #---->dict
d2={4:'d',5:'e'}
d=ChainMap(d1,d2)
print(d.maps)
from collections import ChainMap
L1=[21,20,31,30,41,40,51,50] #---->list
L2=[21,40,55,77]
L=ChainMap(L1,L2)
print(L.maps)
#COUNTER MODULES
from collections import Counter
a=[1,1,2,5,1,4,2,5,4,1,9,7,3,5,3]
A=Counter(a)
print(A)
b=['J','A','N','A','R','T','H','A','N','A','N']
A1=Counter(b)
print(A1)


