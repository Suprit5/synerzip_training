from array import array as arr
# newarr=arr('i',[])
values=int(input('Enter the values you want to insert into the array:- '))
# for i in range(values):
#     nums=int(input('Enter the numbers:- '))
#     newarr.append(nums)
# print(newarr)

counter=1
newarr1=arr('i',[])
while counter<=values:
    nums=int(input('Enter the values'))
    newarr1.append(nums)
    counter+=1
print(newarr1)