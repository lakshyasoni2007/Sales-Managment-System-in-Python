import pandas as pd
from datetime import date
import csv
import matplotlib.pyplot as plt
import sys


    
def main():
    print("1. User  2. Manager  3.Exit")
    c= input('Enter Choice : ')
    if c=="1":
        user()
    elif c=='2':
        p= input('Enter Password : ')
        if p== '3443':
            manager()
        else:
            print("Incorrect Password")
            main()
    elif c=='3':
        sys.exit("Exiting The Program :) ")
    else:
        main()
def user():
    print('1. Check Products.   2. Buy. 3. Cancel.  4.Exit.')
    c = input('Enter Choice :')
    if c== '1':
        cproducts()
    elif c =='2':
        buy()
    elif c=='3':
        cancel()
    elif c=='4':
        main()
    else:
        user()
def cproducts():
    l=r'E:\Sales Managment System\products.csv'
    with open(l,'r')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x=list(cd.loc[i])
            print('PID : ',i)
            print('NAME : ',x[0])
            print('COST : ',x[1])
            print('REMARKS : ',x[2])
            print('|-------------------------------------|')
        cf.close()
        user()
def buy():
    p=input('Product ID: ')
    n=input('Your Name : ')
    a=input('Address : ')
    t = date.today()
    row = [p,n,a,t]
    print('Kindly Pay On Delivery')
    ol =r'E:\Sales Managment System\oders.csv'
    with open(ol,'a+',newline='')as cf:
        cw = csv.writer(cf)
        cw.writerow(row)
    cf.close()
    user()
def cancel():
    p=input('Product ID : ')
    n = input('Your Name : ')
    a = input('Address : ')
    t= input('Date')
    row=[p,n,a,t]
    l = r'E:\Sales Managment System\oders.csv'
    with open(l,'r+')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        for i in cd.index:
            x = list(cd.loc[i])
            if row== x:
                cd.drop([i],inplace=True)
        cf.close
        with open(l,'w',newline='') as cf:
            cw=csv.writer(cf)
            for i in cd.index:
                x = list(cd.loc[i])
                cw.writerow(x)
        cf.close()
    user()
def manager():
    print('1. Add.  2. Products.    3. Delete.  4. Check Order.  5. Show Sales Graph.    6.exit')
    c=input('Enter Choice : ')
    if c == '1':
        add()
    elif c=='2':
        products()
    elif c=='3':
        delete()
    elif c=='4':
        coders()
    elif c=='5':
        sales_plot()
    elif c=='6':
        main()
    else:
        manager()
def add():
    n=input('Name : ')
    c = input('Cost : ')
    d = input('Details : ')
    row = [n,c,d]
    l=r'E:\Sales Managment System\products.csv'
    with open(l,'a+',newline='')as cf:
        cw =csv.writer(cf)
        cw.writerow(row)
    cf.close()
    manager()
def products():
    l=r'E:\Sales Managment System\products.csv'
    with open(l,'r')as cf:
        cw= csv.reader(cf)
        cd= pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x = list(cd.loc[i])
            print('PID : ',i)
            print('NAME : ',x[0])
            print('COST : ',x[1])
            print('REMARKS : ',x[2])
            print('|-------------------------------------|')
    cf.close()
    manager()
def delete():
    d = int(input('Enter PID : '))
    l= r'E:\Sales Managment System\products.csv'
    with open(l,'r+')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        cd.drop([d],inplace=True)
        cf.close()
        with open(l,'w',newline='') as cf:
            cw = csv.writer(cf)
            for i in cd.index:
                x = list(cd.loc[i])
                cw.writerow(x)
    cf.close()
    manager()
def coders():
    l=r'E:\Sales Managment System\oders.csv'
    with open(l,'r')as cf:
        cw = csv.reader(cf)
        cd = pd.DataFrame(cw)
        print('|-------------------------------------|')
        for i in cd.index:
            x = list(cd.loc[i])
            print('PID : ',x[0])
            print('NAME : ',x[1])
            print('ADDRESS : ',x[2])
            print('DATE : ',x[3])
            print('|-------------------------------------|')
    cf.close()
    manager()

def sales_plot():

    # Load the orders CSV data with tab delimiter and set the column names
    orders_df = pd.read_csv(r'E:\Sales Managment System\oders.csv', delimiter='\t', names=["Product ID", "Name", "Address", "Date"])

    # Load the products CSV data with appropriate column names
    products_df = pd.read_csv(r'E:\Sales Managment System\products.csv', names=["Name", "Cost", "Remarks"])

    # Load the orders CSV data with tab delimiter and set the column names
    orders_df = pd.read_csv(r'E:\Sales Managment System\oders.csv', delimiter='\t', names=["Product ID", "Name", "Address", "Date"])

    # Group the DataFrame by the `Name` column and sum the `Cost` column
    total_sales = products_df.groupby('Name')['Cost'].sum()

    # Create a bar chart of the total sales for each product
    plt.bar(total_sales.index, total_sales.values)
    plt.xlabel('Product Name')
    plt.ylabel('Total Sales')
    plt.title('Total Sales by Product')
    plt.show()
    manager()

main()