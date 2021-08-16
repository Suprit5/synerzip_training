'''
Half Pyramid Pattern of Numbers Pattern: 
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5 
'''
def pattern(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print(j,end='')
        print()

if __name__=='__main__':
    number=int(input('Enter the number:- '))
    pattern(number)