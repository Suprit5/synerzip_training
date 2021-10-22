'''
Reverse Pattern of Digits from 10 Pattern: 
1 
3 2 
6 5 4 
10 9 8 7 
'''
def pattern():
    level = 4
    start=1
    stop=2
    number=2
    for i in range(level):
        for j in range(1,stop):
            print(number-1,end='')
            number+=1       
        stop+=1
        print()

if __name__=='__main__':
    pattern()