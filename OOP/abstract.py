from abc import abstractclassmethod,ABC

class Shapes(ABC):
    @abstractclassmethod
    def area(self):
        return 0

class Rectangle(Shapes):
    def __init__(self):
        self.width=40
        self.length=30
    def area(self):
        return self.width*self.length

#a=Shapes()
b=Rectangle()
print(b.area())