class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name, quantity, price):
        if item_name not in self.inventory:
            self.inventory[item_name] = {'quantity': quantity, 'price': price}
        else:
            self.inventory[item_name]['quantity'] += quantity
            self.inventory[item_name]['price'] = price

    def update_item(self, item_name, quantity, price):
        if item_name in self.inventory:
            self.inventory[item_name]['quantity'] = quantity
            self.inventory[item_name]['price'] = price

    def remove_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]

    def generate_report(self):
        for item_name, item_info in self.inventory.items():
            print(f"Item: {item_name}, Quantity: {item_info['quantity']}, Price: Rs.{item_info['price']}")

# Example inventory:
inventory_manager = Inventory()
inventory_manager.add_item('Laptop', 1, 80000)
inventory_manager.add_item('Phone', 2, 30000)
inventory_manager.update_item('Laptop', 1, 85000)
inventory_manager.remove_item('Phone')
inventory_manager.generate_report()
