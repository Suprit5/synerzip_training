class BikeRental:
    
    def __init__(self,stock=10):
        self.stock=stock

    def availability(self):
        print("Bikes available for rent",self.stock)

    def rent_on_daily_basis(self,quantity):
        self.quantity=quantity
        if self.quantity <= 0:
            print("Enter a positive value")
        elif self.quantity > self.stock:
            print("We are out of stock")
        else:
            self.stock-=self.quantity
            print(f"You have rented {quantity} bikes on daily basis")
        

    def rent_on_weekly_basis(self,quantity):
        if quantity <= 0:
            print("Enter a positive value")
        elif quantity > self.stock:
            print("We are out of stock")
        else:
            self.stock-=quantity
            print(f"You have rented {quantity} bikes on wee basis")

    def rent_on_monthly_basis(self,quantity):
        if quantity <= 0:
            print("Enter a positive value")
        elif quantity > self.stock:
            print("We are out of stock")
        else:
            self.stock-=quantity
            print(f"You have rented {quantity} bikes on monthnly basis")

    def stock1(self,quantity):
        self.stock+=quantity

class Customer:
    def __init__(self):
        self.bikes=0

    def reqbikes(self):
        quantity=0
        try:
            quantity=int(input("Enter the number of bikes required:- "))
        except ValueError as e:
            print('Entered value should be an integer')
        self.bikes+=quantity
        return quantity

    def return_bike(self):
        value=0
        try:
            value=int(input('How many bikes are you returning:- '))
            if value > self.bikes:
                print('Error wrong value')
                value=0
            else:
                self.bikes-=value
        except Exception as e:
            print('Entered value should be an integer')
        return value


# john=BikeRental(20)
# john.availability()
# john.rent_on_daily_basis(2)
# john.availability()
# john.return_bike(2)

# bike=Customer()
# print(bike.return_bike())