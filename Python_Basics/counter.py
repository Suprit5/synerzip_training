'''count nunber of even and odd numbers in a given list'''

def count(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even, odd

list=[21,45,34,89,90,45,76,2,0]
even , odd=count(list)
print(f'Even numbers are {even} and odd numbers are {odd}')

'''count number of upper case and lower case characters'''

def alpha(list1):
    u=0
    l=0
    for i in list1:
        if (i.upper())==i:
            u+=1
        else:
            l+=1
    return u , l

list1=['e','R','r','t']
u,l=alpha(list1)
print(f'Number of uppercase {u} and number of lower case alpha {l}')