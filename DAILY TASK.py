#OUTPUT FORMATTING 
a=50
b=100
X= "I need {} apple for {} rupees"
print(X.format(a,b))
a1= 'you'
b1= 'you will'
X1="The herder {} work for somthing, The Greater {} feel when you achive it."
print(X1.format(a1,b1))
#INDEX METHOD
X1="The herder {1} work for somthing, The Greater {0} feel when you achive it."
print(X1.format(a1,b1))
X= "I need {1} apple for {0} rupees"
print(X.format(a,b))
#KEYWORD METHOD
a2='is'
b2='you'
x2="Dreams {a2} not what {b2} see in sleep"
print(x2.format(a2='is',b2='you'))
#USER INPUT
#STRING
a3=input("Enter the course name")
print(a3+"in chennai")
#INT
a4=int(input("I complete my UG degree in the year of"))
print(a4) 
#FLOAT
a5=float(input("I got final year result with the CGPA"))
print(a5) 



