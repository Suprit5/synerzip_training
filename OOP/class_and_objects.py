'''Objet Oriented Programming Classes and Objects'''
'''Bottom to top approach for understanding'''

class Car:
    def __init__(self,color,model):    #__init__ is a initializing method which doesn't need to be called explicitly
        self.color=color               #Here we are assigning each object a variable
        self.model=model               #Here we are assigning each object a variable
    def list(self):
        print(f'The color of the car is {self.color} and model is {self.model}') #Here we are using self because we are reffering to an object

car1=Car('Red',1998)     #Here we use a constructor to create a object called car1                           |   ^
car2=Car('Gray',2021)    #Here we use a constructor to create a object called car2                           |   |
car1.list()              #Here we are calling a func list to print the detail by passing car1 as an object   |   |
car2.list()              #Here we are calling a func list to print the detail by passing car2 as an object  \ /  |