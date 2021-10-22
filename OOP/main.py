from bike import BikeRental,Customer

def main():
    shop=BikeRental()
    customer=Customer()

    while True:
        print("""====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on daily basis
        3. Request a bike on weekly basis 
        4. Request a bike on monthly basis 
        5. Return a bike
        6. Exit""")
        choice=int(input('Enter your choice:- '))
        if choice == 1:
            shop.availability()
        elif choice == 2:
            shop.rent_on_daily_basis(customer.reqbikes())
        elif choice == 3:
            shop.rent_on_weekly_basis(customer.reqbikes())
        elif choice == 4:
            shop.rent_on_monthly_basis(customer.reqbikes())
        elif choice == 5:
            shop.stock1(customer.return_bike())
        elif choice == 6:
            break
main()