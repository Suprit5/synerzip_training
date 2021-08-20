'''
Reverse Pyramid of Numbers Pattern: 
1  
2 1  
3 2 1  
4 3 2 1  
5 4 3 2 1 
'''
def pattern(number):
    for i in range(1,number+1):
        for j in range(i,0,-1):
            print(j,end='')
        print()


if __name__=='__main__':
    number=int(input("Enter the numbrt"))
    pattern(number)