#VARIABLE ARGUMENTS
def func (a,b):
    print(a+b)
func(12,18) # print numbers
def func(a1,b1):
    print(a1 or b1)
func(a1=True,b1=False) # print as strings
#KEYWORD ARGUMENTS
def func (a,b):
    print(a+b)
func(a=22,b=16)
def func(a1,b1):
    X= "Nirmal is {} passed out and get job in {} at the same year."
    print(X.format(a1,b1))
func(a1=2021,b1="Pharm")
#ARBITARY VARIABLE ARGUMENT:
def func(*a):
    print(a)
func(10,11,20,21,30,31,40,41)
def func(*b):
    print(b)
func(2001,True,"PYTHON",14j,0.10)
#ARBITARY KEYWORD ARGUMENT:    
def func(**kwargs):
    print(kwargs)
func(a1="JAVA",c1="PYTHON",a=10,c=25)
def func (**Electronics):
    print(Electronics)
func(a="PCB",b="NETWORK",c="SECURITY")
#DEFAULT ARUGUMENTS
def func (a='PYTHON'):
    print(a)
func()
func('JAVA')
func("C++")




           