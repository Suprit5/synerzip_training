def factorial(number):
    ans=1
    for i in range(number,0,-1):
        ans=ans*i
    return ans
def r_factorial(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return number*r_factorial(number-1)

number= int(input('Enter the number:- '))
answer=r_factorial(number)
print(f' The factorial of {number} is {answer}')