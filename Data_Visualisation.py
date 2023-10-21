#pip install pandas

import pandas as pd
import matplotlib.pyplot as plt

# Analyze sales trends over time
sales_data['date'] = pd.to_datetime(sales_data['date'])
sales_data.set_index('date', inplace=True)

# line chart for total sales over time
sales_data['total_sales'] = sales_data['quantity'] * sales_data['price']
total_sales_over_time = sales_data.resample('D').sum()
total_sales_over_time['total_sales'].plot(kind='line')
plt.xlabel('Date')
plt.ylabel('Total Sales')
plt.title('Total Sales Over Time')
plt.show()

# Identify peak sales hours and popular products
peak_sales_hour = sales_data.groupby(sales_data.index.hour)['quantity'].sum()
popular_products = sales_data['item'].value_counts()

# Generate reports
print("Peak Sales Hour:")
print(peak_sales_hour.idxmax())
print("Popular Products:")
print(popular_products)

