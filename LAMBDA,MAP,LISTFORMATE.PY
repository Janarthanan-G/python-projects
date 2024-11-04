#LAMBDA:
x=lambda a,b,c:a-b*c
print(x(2,7,11))

y=lambda a,b,c,d:a+b*c/d
print(y(12,18,20,1))

x1=lambda a,b,c,d,e:a%b+c-d*e
print(x1(18,12,4,33,7))

#MAP FUNCTION():

#def myfunc(a,b):
#    return a+b
#x=map(myfunc('orange','white','green'),('red','yellow','blue'))

#LISTFORMATE:
def func(n):
    return(n*n)
numbers=[2,4,6,8,10]
x=list(map(func,numbers))
print(x)
