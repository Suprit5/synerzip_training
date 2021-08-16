'''
Search for even numbers,double the values of an array and sum of all the elements of an array using lambda function.
'''
from functools import reduce

numbers=[56,23,78,0,98,22,35,25,1,6,9]
#Search even numbers from the above list
evens=list(filter(lambda x : x%2==0,numbers))
print(f'list of even numbers from the given list {evens}')

#double the values of the second list called evens
doubles=list(map(lambda x : x*2,evens))
print(f'List after doubling all the values from the evens list {doubles}')

#sum of all the values from the double list
total=reduce(lambda a,b : a+b,doubles)
print(f'Sum of all the elements from the elements double is {total}')