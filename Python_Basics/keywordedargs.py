def person(name,**data):
    print(name)
    for i,j in data.items():
        print(i,':',j)

person('suprit',age=23,salary='10k',location='mumbai')