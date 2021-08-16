'''
Simple Number Triangle Pattern Pattern: 
1   
2 2   
3 3 3   
4 4 4 4   
5 5 5 5 5 
'''
def pattern(number):
    for i in range(1,number+1):
        for j in range(i):
            print(i,end='')
        print()

if __name__=='__main__':
    #number=int(input('Enter the number:- '))
    pattern(5)