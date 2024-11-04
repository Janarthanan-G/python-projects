#TO FIND THE MINIMUM OF THREE NUMBERS IN A LIST:
l = [20,1,4,22,305,210,45]
l.sort()
l1=[]
if len(l)<=3:
    print("list is less than 3 elements")
else:
    for i in range(3):
        l1.append(l[i])
print(l1)

#CAPITALIZE THE FIRST LETTER OF EACH WORD IN A SENTENCE:
txt = "i complete my ug degree in the college of kumaraguru."
A= txt.title()
print (A)

#REVERSE THE LIST OF NUMBER:
numbers = [0.2, 0.56, 1.1, 2.1, 3, 3.01, 3.32, 5]
rev_num = numbers[::-1]  
print(rev_num)

#DELETE, REMOVE, POP IN LIST():
A1=[11,22,33,44,55,66,77,88]
del A1[2]
print(A1)
A1.remove(44)
print(A1)
pop_value=A1.pop(5)
print(A1)

# INIT FUNCTIONS:
class A:
    def __init__(self, a):
        self._a = a  
        print(a)  
    def get_a(self):
        return self._a  
obj = A(5)  
print("Value:", obj.get_a()) 

#BREAKE AND CONTIUES:
for i in range(12):
  if i > 7:
    break
  print(i)

for i in range(12):
  if i == 7:
    continue
  print(i)

#LAMBDA:
x=lambda a,b,c:a-b*c
print(x(2,7,11))
y=lambda a,b,c,d:a+b*c/d
print(y(12,18,20,1))
x1=lambda a,b,c,d,e:a%b+c-d*e
print(x1(18,12,4,33,7))

