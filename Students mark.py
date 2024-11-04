
#Student Mark Statements

A=int(input("My final year overall percentage I get  marks"))

if(A==100):
    print("Students got good percentage with O grade")
elif(90<A & A<=99):
    print("Students got good percentage with A+ grade")  
elif(80<=A & A<=90):
    print("Students got good percentage with A grade")     
elif(70<=A & A<80):
    print("Students got good percentage with B grade")    
elif(60<=A & A<70):
    print("Students got good percentage with C grade")
elif(50<=A & A<60):
    print("Students got good percentage with D grade")         
else:
    print("Students got Fail marks")