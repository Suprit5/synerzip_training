'''There are two type of variable class variable and instance variable'''
'''The class variable are static variable and instance variable are associated with objects'''

class Car:
    wheels=5        #Static Value
    def detail(self,name,year,color):
        print(f'The car name is {name} from {year} in {color} color has {self.wheels} wheels')

car1=Car()
car2=Car()
car3=Car()

car3.wheels=6

car1.detail('Toyota',2012,'Red')            #Instance Variable
car2.detail('Suzuki',2015,'Gray')           #Instance Variable
car3.detail('Mitsubshi',2004,'Yellow')      #Instance Variable