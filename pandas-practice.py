import pandas as pd
import matplotlib.pyplot as plt

sales_data = pd.read_csv('sales.csv')
print(sales_data)
type(sales_data)

#Read data headers
print(sales_data.columns)

#Summary statistics of data, including mean, min and max.
print(sales_data.describe())

#Sum of sales across the year:
total_sales = sales_data['sales'].sum()
print('The total sales across 2018 are:')
print(total_sales)

#Plot of sales and expenditure over 2018:
plt.plot(sales_data.month, sales_data.sales)
plt.plot(sales_data.month, sales_data.expenditure)
plt.title('Sales & Expenditure across 2018')
plt.xlabel('Month')
plt.ylabel('Sales/Expenditure')
plt.grid(True)
plt.show()



