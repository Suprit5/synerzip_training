arr1=[34,123,54,57,23]
arr2=[352,234,67,9,6743,12]

for i in range(len(arr2)):
    remove=arr2.pop(0)
    arr1.append(remove)
print(arr1)