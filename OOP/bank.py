class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def show_detail(self):
        print("::::::User details::::::")
        print("Name:- ",self.name)
        print("Age:- ",self.age)
        print("Gender:- ",self.gender)
class Bank(User):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    
    def deposit(self,amount):
        self.amount=amount
        self.balance=self.balance+self.amount
        print(f"{self.name} your account balance is {self.balance}")     

    def withdraw(self,amaount):   
        self.amount = amaount
        self.balance=self.balance-self.amount
        if self.amount > self.balance:
            print(f"Insufficient balance:- {self.balance}")
        else:
            print(f"Your balance after withdraw is {self.balance}")


# john = User('Suprit',23,"M")
# john.show_detail()
john=Bank('John',44,'M')
john.deposit(56)
john.withdraw(40)
john.deposit(4)