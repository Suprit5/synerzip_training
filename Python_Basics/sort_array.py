# array=[45,23,13,56,78,53,7,0]
# for i in range(0,len(array)):
#     for j in range(i,len(array)):
#         if array[i]>array[j]:
#             array[i],array[j]=array[j],array[i]
# print(f'Maximum value in array is:- {array[-1]}')

'''move all the zero towards the end of an array'''
array1=[0,34,56,0,31,0,56,0,11]
count=0
for i in range(0,len(array1)):
    if array1[i]!=0:
        array1[count],array1[i]=array1[i],array1[count]
        count+=1
print(array1)