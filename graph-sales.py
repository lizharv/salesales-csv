import os
os.system('pip install matplotlib')
os.system('pip install pandas')

import csv

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style



with open('sales.csv', 'r') as csv_file:
    sales_reader = csv.reader(csv_file)

    for line in sales_reader:
        print(line)

def readdata():
    data=[]
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return(data)


def total_sales():
    data=readdata()
    sales=[]
    for row in data:
        sale=int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print('Total Sales: {}'.format(total))

total_sales()


def avg_sales():
    data=readdata()
    sales=[]
    for row in data:
        sale=int(row['sales'])
        sales.append(sale)
    average = sum(sales)/len(sales)
    print('Average Sales: {}'.format(average))

avg_sales()




def sales_plot():
    data=readdata()
    sales=[]
    df = pd.DataFrame(data, columns=['month', 'sales'])
    plt.plot(df['month'], df['sales'], color='red', marker='o')
    plt.title('Sales per Month, 2018', fontsize=14)
    plt.xlabel('Month', fontsize=14)
    plt.ylabel('Sales', fontsize=14)
    plt.grid(True)
    plt.show()
sales_plot()



"""df = df.sort_values('sales')
    df = pd.DataFrame(list(zip(df['sales'], df['month']))).set_index(1)
    df.plot.bar()
    plt.show()
sales_plot()"""