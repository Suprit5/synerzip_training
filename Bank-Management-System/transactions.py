from database import *
import prettytable

class Transactions():
    def __init__(self):
        self.sending_acc = int(input('Enter Your Account Number:- '))
        self.recieving_acc = int(input('Enter Recipient Account Number:-'))
        self.amount=int(input('Enter Amount:- '))

    def customer_transaction(self):
        bank_db=accessing_db()
        bank=bank_db.cursor()
        bank.execute(f'''
        UPDATE savings_account
        SET balance = CASE acno
        WHEN {self.sending_acc} THEN balance - {self.amount}
        WHEN {self.recieving_acc} THEN balance + {self.amount}
        END
        WHERE acno IN ({self.sending_acc},{self.recieving_acc});
        ''')
        bank_db.commit()


hi=Transactions()
hi.customer_transaction()