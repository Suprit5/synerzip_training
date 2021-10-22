import mysql.connector
import prettytable
from datetime import time
from datetime import date
from datetime import datetime
x=input("enter username:- ")
y=input("enter password:- ")
mydb=mysql.connector.connect(host="localhost",user="%s"%x,password="%s"%y,)
mycursor=mydb.cursor()
today=date.today()
d2=today.strftime("%A,%B %d, %Y")
t = datetime.time(datetime.now())
print("Todays Date:-\t", d2,"Time:-\t",t)
print("WELCOME TO WAREHOUSE DATABASE")
print("1.Insert Data\n2.Delete Data\n3.Update Data\n4.View Products\n5.Search")
x=input("Enter Your Choice:- ")
mycursor.execute("create database if not exists warehouse")
mycursor.execute("use warehouse")
mycursor.execute("create table if not exists BHIWANDI(Item_No int not null auto_increment primary key,Product_ID int unique key,Product_Name varchar(255),Category varchar(255),Qty int,Price int,Location varchar(255))")
mycursor.execute("create table if not exists THANE(Item_No int not null auto_increment primary key,Product_ID int unique key,Product_Name varchar(255),Category varchar(255),Qty int,Price int,Location varchar(255))")
mycursor.execute("create table if not exists BANDRA(Item_No int not null auto_increment primary key,Product_ID int unique key,Product_Name varchar(255),Category varchar(255),Qty int,Price int,Location varchar(255))")
mycursor.execute("create table if not exists AMBERNATH(Item_No int not null auto_increment primary key,Product_ID int unique key,Product_Name varchar(255),Category varchar(255),Qty int,Price int,Location varchar(255))")
def insert():
    mycursor=mydb.cursor()
    mycursor.execute("use warehouse")
    mycursor.execute("show tables")
    tables=mycursor
    print(prettytable.from_db_cursor(tables))
    warehouse=input("IN WHICH WAREHOUSE YOU WANT TO ENTER DATA?\t")
    mycursor.execute("select * from %s"%warehouse)
    s=mycursor
    print(prettytable.from_db_cursor(s))
    mycursor.execute("use warehouse")
    id=input("Enter Product Id:- ")
    pname=input("Enter Product Name:- ")
    cat=input("Enter Category:- ")
    q=input("Enter Quantity:- ")
    p=input("Enter Price:- ")
    loc=input("Enter Location:- ")
    mycursor.execute("insert into {0} values(NULL,'{1}','{2}','{3}','{4}','{5}','{6}')".format(warehouse,id,pname,cat,q,p,loc))
    mydb.commit()
def delete():
    mycursor=mydb.cursor()
    mycursor.execute("use warehouse")
    mycursor.execute("show tables")
    tables=mycursor
    print(prettytable.from_db_cursor(tables))
    warehouse=input("FROM WHICH DATABASE YOU WANT TO REMOVE THE PRODUCT?\t")
    mycursor.execute("select * from %s"%warehouse)
    s=mycursor
    print(prettytable.from_db_cursor(s))
    con=input("Enter Product ID:- ")
    mycursor.execute("delete from {0} where Product_ID = '{1}' ".format(warehouse,con))
    mycursor.execute("ALTER TABLE %s DROP Item_No"%warehouse)
    mycursor.execute("ALTER TABLE %s ADD Item_No int not null auto_increment primary key first;"%warehouse)
    mydb.commit()
    mycursor.execute("use warehouse")
    mycursor.execute("select * from %s"%warehouse)
    st=mycursor
    print(prettytable.from_db_cursor(st))
def update():
    mycursor=mydb.cursor()
    mycursor.execute("use warehouse")
    mycursor.execute("show tables")
    tables=mycursor
    print(prettytable.from_db_cursor(tables))
    warehouse=input("WHICH WAREHOUSE PRODUCT YOU WANT TO UPDATE?\t")
    mycursor.execute("select * from %s"%warehouse)
    s=mycursor
    print(prettytable.from_db_cursor(s))
    id=input("Enter Product Id:- ")
    qty=input("Enter Updated Quantity:- ")
    price=input("Enter Updated Price:- ")
    mycursor.execute("UPDATE {0} SET Qty = {1},Price={2} WHERE Product_ID ='{3}'".format(warehouse,qty,price,id))
    mydb.commit()
    mycursor.execute("use warehouse")
    mycursor.execute("select * from %s"%warehouse)
    st=mycursor
    print(prettytable.from_db_cursor(st))
def view():
    mycursor=mydb.cursor()
    mycursor.execute("use warehouse")
    mycursor.execute("show tables")
    tables=mycursor
    print(prettytable.from_db_cursor(tables))
    tview=input("WHICH WAREHOUSE PRODUCT YOU WANT TO VIEW?\t")
    mycursor.execute("select * from %s"%tview)
    s=mycursor
    print(prettytable.from_db_cursor(s))
def search():
    mycursor=mydb.cursor()
    mycursor.execute("use warehouse")
    chi=''
    while (chi.upper())!='Q':
        chi=input("SEACH BY\n 1.PRODUCT ID \n 2.CATEGORY\n 3.PRODUCT NAME\nEnter Your Choice:- ")
        if chi=='1':
            mycursor=mydb.cursor()
            mycursor.execute("use warehouse")
            mycursor.execute("show tables")
            t=mycursor
            print(prettytable.from_db_cursor(t))
            wname=input("Which Warehouse:- ")
            id=input("Enter Product ID:- ")
            mycursor.execute("select * from {0} where Product_ID={1}".format(wname,id))
            d=mycursor
            print(prettytable.from_db_cursor(d))
        elif chi=='2':
            mycursor=mydb.cursor()
            mycursor.execute("use warehouse")
            mycursor.execute("show tables")
            t=mycursor
            print(prettytable.from_db_cursor(t))
            wname=input("Which Warehouse:- ")
            cat=input("Enter Category:- ")
            mycursor.execute("select * from {0} where Category='{1}'".format(wname,cat))
            d=mycursor
            print(prettytable.from_db_cursor(d))
        elif chi=='3':
            mycursor=mydb.cursor()
            mycursor.execute("use warehouse")
            mycursor.execute("show tables")
            t=mycursor
            print(prettytable.from_db_cursor(t))
            wname=input("Which Warehouse:- ")
            pname=input("Enter Product Name:- ")
            mycursor.execute("select * from {0} where Product_Name={1}".format(wname,pname))
            d=mycursor
            print(prettytable.from_db_cursor(d))
        else:
            print("Wrong Input")
if x=='1':
    insert()
    ch=''
    while (ch.upper())!='N':
        ch=input("Do You Want To Enter More Enteries?(Y/N)")
        if (ch.upper())=='Y':
            insert()
            print("Data Entered Successfully")
        else:
            print("BYE")
if x=='2':
    delete()
    ch=''
    while (ch.upper())!='N':
        ch=input("Do You Want To Delete More Enteries?(Y/N)")
        if (ch.upper())=='Y':
            delete()
            print("Data Deleted Successfully")
        else:
            print("BYE")
if x=='3':
    update()
    ch=''
    while (ch.upper())!='N':
        ch=input("Do You Want To Update More Enteries?(Y/N)")
        if (ch.upper())=='Y':
            update()
            print("Data Updated Successfully")
        else:
            print("BYE")
if x=='4':
    view()
if x=='5':
    search()
