def fibonacci(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n):
        d=a
        a=b
        b=a+d
        print(b)
    return b
def r_fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return r_fibonacci(n-2)+r_fibonacci(n-1)

number=int(input('Enter the number:- '))
answer=fibonacci(number)
print(f'te fibonacci sequence of {number} is {answer}')