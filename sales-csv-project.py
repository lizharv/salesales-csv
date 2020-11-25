import os
os.system('pip install plotly')
os.system('pip install matplotlib')

from matplotlib import pyplot as plt
from matplotlib import style

import csv

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


"""matplotlib.plot(month, sales)
matplotlib.title('Sales per Month, 2018')
matplotlib.xlabel('Month')
matplotlib.ylabel('Sales')
matplotlib.show()"""

style.use('ggplot')

