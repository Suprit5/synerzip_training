def moveApples(input1,input2):
    avg=sum(input2)//input1
    result =0
    for i in range(input1):
        print('abs-->',abs(avg-input2[i]))
        result+=abs(avg-input2[i])
    return result//2

print('final->',moveApples(5, [2849,1620,705,1,30]))