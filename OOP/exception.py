'''
Exception handling helps to handle run-time error efficiently.
Run-time error are the error which occurs because of the end users.
Exception handling has 3 main blocks try, except and finally:-
-> In try block we enter the part of the code which might lead to some trouble.
-> In except block we can define different types of error which might occur and to cover all the error we can use Exception
-> The finally block helps the complete execution of the code 
'''

try:
    a=int(input("Enter the first number:- "))
    b=int(input("Enter the second number:- "))
    print("Port open!")
    print(a/b)

except ZeroDivisionError as e:
    print("Can't divide a number a number by zero",e)

except ValueError as e:
    print("Entered value must be an integer",e)

except Exception as e:
    print('Error', e)

finally:
    print("Port closed!")