"""Without using any string methods, try to print the following: 12345 take a number as an input and generate 
a string"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1,n+1):
        print(i,end="")
