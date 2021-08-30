'''
Inverted Half Pyramid Number Pattern 
Pattern: 
0 1 2 3 4 5  
0 1 2 3 4  
0 1 2 3  
0 1 2  
0 1
'''
def pattern(number):
    for i in range(number,0,-1):
        for j in range(0,i+1):
            print(j,end='')
        print()

if __name__=='__main__':
    number=int(input('Enter the number:- '))
    pattern(number)