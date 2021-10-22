class A:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    
    def __add__(self,other):
        b1=self.m1+other.m1
        b2=self.m2+other.m2
        return b1,b2



a1=A(90,89)
a2=A(65,45)

print(a1+a2)