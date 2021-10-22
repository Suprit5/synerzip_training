'''
Pyramid of Natural Numbers Less Than 10 
Pattern: 
1  
2 3 4  
5 6 7 8 9
'''
def pattern(number):
    level = int((number/2)-2)
    start=1
    stop=2
    for i in range(level):
        for j in range(1,stop):
            print(start,end='')
            start+=1
        print()
        stop+=2
        

if __name__=='__main__':
    pattern(10)