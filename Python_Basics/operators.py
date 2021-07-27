def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def div(a,b):
    return a/b

def fdiv(a,b):
    return a//b

if __name__=="__main__":
    a=int(input("Enter the 1st number:-"))#tycapsting and taking the user input 
    b=int(input("Enter the 2nd number:-"))
    print("Addition: ",add(a,b))
    print("Substraction: ",sub(a,b))
    print("Division: ",div(a,b))
    print("Floor Division: ",fdiv(a,b))