class SalesDatabase:
    def __init__(self):
        self.sales_data = []

    def record_sale(self, customer_name, purchased_items):
        sale = {'customer_name': customer_name, 'purchased_items': purchased_items}
        self.sales_data.append(sale)

    def calculate_total_sales(self, period):
        total_sales = 0
        for sale in self.sales_data:
            # Assuming date is included in each sale
            sale_date = sale['date']
            if period[0] <= sale_date <= period[1]:
                for item in sale['purchased_items']:
                    total_sales += item['quantity'] * item['price']
        return total_sales

    def provide_discounts(self, customer_name, discount):
        for sale in self.sales_data:
            if sale['customer_name'] == customer_name:
                for item in sale['purchased_items']:
                    item['price'] -= (item['price'] * discount)

    def generate_customer_report(self):
        customer_sales = {}
        for sale in self.sales_data:
            customer_name = sale['customer_name']
            if customer_name not in customer_sales:
                customer_sales[customer_name] = 0
            for item in sale['purchased_items']:
                customer_sales[customer_name] += item['quantity'] * item['price']

        sorted_customers = sorted(customer_sales.items(), key=lambda x: x[1], reverse=True)
        print("Top Customers:")
        for customer, total_sales in sorted_customers:
            print(f"{customer}: Rs. {total_sales}")

# Example database:
sales_db = SalesDatabase()
sales_db.record_sale('Rohan', [{'item': 'Laptop', 'quantity': 1, 'price': 850000}, {'item': 'Phone', 'quantity': 1, 'price': 20000, 'date': '2023-10-15'}])
sales_db.record_sale('Aryan', [{'item': 'Tablet', 'quantity': 3, 'price': 200000, 'date': '2023-10-14'}])
sales_db.provide_discounts('Rohan', 0.1)
sales_db.generate_customer_report()
