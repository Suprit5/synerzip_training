""" The provided code stub reads and integer, n, from STDIN. For all non-negative integers i<n, print i^2. """

import math
def square(n):
    for i in range(n):
        j=pow(i,2)
        print(j)

if __name__ == '__main__':
    n = int(input())
    square(n)