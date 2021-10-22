from database import *
import prettytable

def savings_account():
    bank_db=accessing_db()
    bank=bank_db.cursor()
    print('--------Enter the following details--------')
    name=input('Enter Full Name :- ')
    address=input('Enter The Address:- ')
    p_number=int(input('Enter Phone Number:- '))
    email=input('Enter email:- ')
    aadhar_no=int(input('Enter Aadhar Number:- '))
    bank.execute(f'''INSERT INTO savings_account 
    (name, address, phone_no, email, aadhar_no) 
    VALUES ("{name}","{address}",{p_number},"{email}",{aadhar_no})
    ''')
    bank_db.commit()

def salary_account():
    bank_db=accessing_db()
    bank=bank_db.cursor()
    '''
    acno int not null auto_increment primary key, 
    company_id varchar(20), 
    name char(30), 
    address varchar(100), 
    phone_no int not null unique, 
    email varchar(80) unique, 
    aadhar_no int not null unique, 
    acc_type char(30) DEFAULT "Salary Account", 
    status varchar(10), 
    balance int not null)
    '''
    print('--------Enter the following details--------')
    company_id=input('Enter Company ID:- ')
    name=input('Enter Full Name :- ')
    address=input('Enter The Address:- ')
    p_number=int(input('Enter Phone Number:- '))
    email=input('Enter email:- ')
    aadhar_no=int(input('Enter Aadhar Number:- '))
    bank.execute(f'''INSERT INTO salary_account 
    (company_id, name, address, phone_no, email, aadhar_no) 
    VALUES ("{company_id}","{name}","{address}",{p_number},"{email}",{aadhar_no})
    ''')
    bank_db.commit()

def account_type():
    print('''
    ----------Account Type-----------
    ------------Options--------------
    1. Savings Account.
    2. Salary Account.
    ''')
    choice=int(input('Enter the option number:- '))
    if choice == 1:
        savings_account()
    elif choice == 2:
        salary_account()

def search_account(table_name):
    bank_db=accessing_db()
    bank=bank_db.cursor()
    while True:
        print('''
        --------Search By--------
        1. Account Number.
        2. Name.
        3. Aadhar Number.
        4. Phone Number.
        ''')
        choice=int(input('Enter The Number:- '))
        if choice == 1:
            attribute='acno'
            account_no = int(input('Enter Account Number:- '))
            bank.execute(f'''
            SELECT * FROM {table_name}
            WHERE {attribute} = {account_no}
            ''')
            print(prettytable.from_db_cursor(bank))
            return account_no,attribute
        elif choice == 2:
            attribute='name'
            name = input('Enter Name:- ')
            bank.execute(f'''
                SELECT * FROM {table_name}
                WHERE {attribute} = '{name}'
                ''')
            print(prettytable.from_db_cursor(bank))
            return name,attribute
        elif choice == 3:
            attribute='aadhar_no'
            aadhar_no = int(input('Enter Aadhar Number:- '))
            bank.execute(f'''
            SELECT * FROM {table_name}
            WHERE {attribute} = {aadhar_no}
            ''')
            print(prettytable.from_db_cursor(bank))
            return aadhar_no,attribute
        elif choice == 4:
            attribute='phone_no'
            phone_no = int(input('Enter phone number:- '))
            bank.execute(f'''
                SELECT * FROM {table_name}
                WHERE {attribute} = {phone_no}
                ''')
            print(prettytable.from_db_cursor(bank))
            return phone_no,attribute
           
def delete_account():
    bank_db=accessing_db()
    bank=bank_db.cursor()
    
    while True:
        print('''
    --------Select Option--------
    1. Delete A Account From Savings Account.
    2. Delete A Account From Salary Account.
    ''')
        choice=int(input('Enter The Number:- '))
        if choice == 1:
            value, attribute = search_account('savings_account')
            print('''
            --------Do You Want To Delete This Account?--------
            1. Yes.
            2. No.
            ''')
            choice = int(input('Enter The Number'))
            if choice == 1:
                if type(value)== int:
                    bank.execute(f'''
                    DELETE FROM savings_account
                    WHERE {attribute} = {value}
                    ''')
                    bank_db.commit()
                else:
                    bank.execute(f'''
                    DELETE FROM savings_account
                    WHERE {attribute} = '{value}'
                    ''')
                    bank_db.commit()

            else:
                accounts()
        
        elif choice == 2:
            value, attribute = search_account('salary_account')

            print('''
            --------Do You Want To Delete This Account?--------
            1. Yes.
            2. No.
            ''')
            choice = int(input('Enter The Number'))
            if choice == 1:
                if type(value)== int:
                    bank.execute(f'''
                    DELETE FROM salary_account
                    WHERE {attribute} = {value}
                    ''')
                    bank_db.commit()
                else:
                    bank.execute(f'''
                    DELETE FROM salary_account
                    WHERE {attribute} = '{value}'
                    ''')
                    bank_db.commit()

            else:
                accounts()

def accounts():
    while True:
        print('''
        ------------Options--------------
        1. Create A New Account.
        2. Delete Account.
        ''')
        choice=int(input('Enter the option number:- '))
        if choice == 1:
            account_type()
        elif choice == 2:
            delete_account()

if __name__ == '__main__':
    search_account('savings_account')