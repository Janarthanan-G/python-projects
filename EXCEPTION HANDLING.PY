#EXCEPTION HANDLING
#TRY,EXCEPT,ELSE,FINALLY
def division(a,b):
    try:
        result=b/a
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

division(20,100)    
