# """pattern-1"""
# for i in range(5):
#     for i in range(4):
#         print("#",end="")
#     print()

# """pattern1-2"""
# for i in range(1,6):
#     for i in range(i):
#         print("#",end="")
#     print()

# """pattern1-3"""
# for i in range(6,0,-1):
#     for i in range(i):
#         print("#",end="")
#     print()

# for i in range(1,5):
#     for j in range(i,5):
#         print(j,end='')
#     print()


# num=6
# for i in range(1,num+1):
#     nums=num-1
#     for k in range(nums,0,-1):
#         print(' ',end='')
#     for j in range(1,i+1):
#         print('*',end='')
#     num-=1
#     print()

# num=7
# nums=num
# space=int((nums-1)/2)
# for i in range(1,num+1,2):
#     for j in range(space,0,-1):
#         print("/",end='')
#     for k in range(1,i+1):
#         print("*",end='')
#     space-=1
#     num-=1
#     print()

# num=7
# space=int((num-1)/2)
# for i in range(1,num+1,2):
#     for j in range(space,0,-1):
#         print(" ",end='')
#     for k in range(1,i+1):
#         print("*",end='')
#     space-=1
#     num-=1
#     print()
# space=1
# num=int((num*2)-1)
# for i in range(num,0,-2):
#     for j in range(1,space+1):
#         print(" ",end='')
#     for k in range(i,0,-1):
#         print("*",end='')
#     space+=1
#     num-=1
#     print()

nums=4
space=int(nums-1)
print(space)
for k in range(1,nums+1):           #k=1
    for i in range(space,0,-1):     #i=3
        print('/',end='')           
    for j in range(k,0,-1):         #j=1
        print(j,end='')
    for l in range(2,k+1):          #
        print(l,end='')
    space-=1
    print()