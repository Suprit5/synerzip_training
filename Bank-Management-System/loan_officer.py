from database import *
from account_section import search_account
import prettytable

class Loan():

    def give_loan(self):
        bank_db=accessing_db()
        bank=bank_db.cursor()
        while True:
            print('''
            1. Check User Account Detail.
            2. Give Loan.
            ''')
            choice = int(input('Enter The Number:- '))
            if choice == 1:
                value,attribute = search_account('savings_account')
            
            elif choice ==2:
                pass

    def loan(self):
        bank_db=accessing_db()
        bank=bank_db.cursor()
        print('''
        --------Select Option--------
        1. Give Loan.
        2. View Loan.
        ''')
        choice = int(input('Enter The Number:- '))
        if choice == 1:
            hi.give_loan()
        elif choice == 2:
            print('''
            --------Enter Customer Details--------
            ''')
            acc_no = int(input('Enter Customer\'s Account Number:- '))
            name = input('Enter Customer\'s Name:- ')
            aadhar_no = int(input('Enter Customer\'s Aadhar Number:- '))
            g_name = input('Guarantor\'s Name:- ')
            g_p_no = int(input('Enter Guarantor\'s Phone Number:- '))
            g_aadhar_no = int(input('Enter Guarantor\'s Aadhar Number:- '))
            tenure = int(input('Enter Tenure In Mobths:- '))
            roi = float(input('Enter ROI:- '))
            loan_amt = int(input('Enter The Loan Amount:- '))
            bank.execute(f'''
            INSERT INTO loan_details
            VALUES ({acc_no} , '{name}' , {aadhar_no} , {loan_amt} , {tenure} , {roi} , '{g_name}' , {g_p_no} , {g_aadhar_no})
            ''')
            bank_db.commit()

hi=Loan()
hi.loan()
