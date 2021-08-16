'''
Inverted Pyramid of Descending Numbers Pattern: 
5 5 5 5 5  
4 4 4 4  
3 3 3  
2 2  
1
'''
def pattern(number):
    for i in range(number,0,-1):
        for j in range(i):
            print(i,end='')
        print()

if __name__=='__main__':
    number=int(input('Enter the number:- '))
    pattern(number)