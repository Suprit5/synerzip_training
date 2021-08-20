'''Inverted Pyramid of the Same Digit Pattern: 
5 5 5 5 5  
5 5 5 5  
5 5 5  
5 5  
5 
'''
def pattern(number):
    for i in range(number,0,-1):
        for j in range(i):
            print(number,end='')
        print()

if __name__=='__main__':
    number=int(input('Enter the number:- '))
    pattern(number)