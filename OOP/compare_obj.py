class Person:
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age
        
    def detail(self,name,age):
        self.name=name
        self.age=age
        person_1.age=30
        print(f'My name is {name} and my age is {age}')
    
    def compare(self,person_2):
        if self.age==person_2.age:
            return True
        else:
            return False

person_1=Person()
person_2=Person()

person_1.detail('Rahul',23)
person_2.detail('Sanjay',23)

if person_1.compare(person_2):
    print('They have same age')
else:
    print('They dont have same age')