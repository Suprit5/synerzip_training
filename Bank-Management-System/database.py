import mysql.connector as sql


def accessing_db():
    #username=input('Enter the username:- ')
    #password=input('Enter the password:- ')
    bank_db=sql.connect(host='localhost',user='root', password='6657')
    creating_tables(bank_db)
    return bank_db

def creating_tables(bank_db):
    bank=bank_db.cursor()
    bank.execute('create database if not exists bank')
    bank.execute('use bank')
    bank.execute('create table if not exists savings_account(acno int not null auto_increment primary key, name char(30), address varchar(100), phone_no bigint not null unique, email varchar(80) unique, aadhar_no bigint not null unique, acc_type char(30) DEFAULT "Savings Account", status varchar(10), balance int not null DEFAULT 0)')
    bank.execute('create table if not exists salary_account(acno int not null auto_increment primary key, company_id varchar(20), name char(30), address varchar(100), phone_no bigint not null unique, email varchar(80) unique, aadhar_no bigint not null unique, acc_type char(30) DEFAULT "Salary Account", status varchar(10), balance int not null DEFAULT 0)')
    bank.execute('create table if not exists loan_details(acno int not null primary key, name char(40), aadhar_no int unique, guarantor_name char(40), guarantor_number int unique, guarantor_aadhar_no int unique, loan_amount int, tenure int,roi float(4))')
    bank.execute('create table if not exists ledger(date datetime, acno int primary key, sent_to varchar(100) not null, received_from varchar(100), withdrawl_amt int, deposited_amt int, current_bal int )')


if __name__=='__main__':
    accessing_db()