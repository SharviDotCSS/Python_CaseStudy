import tkinter as tk

class StoreGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Retail Store")

        self.cart = []
        self.products = {
            'Laptop': 80000,
            'Phone': 300000,
            'Tablet': 200000
        }

        self.create_ui()

    def create_ui(self):
        # product labels, buttons, and quantity entry
        for product, price in self.products.items():
            product_frame = tk.Frame(self.root)
            product_label = tk.Label(product_frame, text=f"{product} - Rs. {price}")
            product_label.pack(side=tk.LEFT)
            quantity_label = tk.Label(product_frame, text="Quantity:")
            quantity_label.pack(side=tk.LEFT)
            quantity_entry = tk.Entry(product_frame, width=5)
            quantity_entry.insert(0, "1")  # Set default quantity to 1
            quantity_entry.pack(side=tk.LEFT)
            product_button = tk.Button(product_frame, text="Add to Cart", command=lambda p=product, price=price, entry=quantity_entry: self.add_to_cart(p, price, entry))
            product_button.pack(side=tk.LEFT)
            product_frame.pack()

        # cart label and clear cart button
        self.cart_label = tk.Label(self.root, text="Cart: ")
        self.cart_label.pack()

        clear_cart_button = tk.Button(self.root, text="Clear Cart", command=self.clear_cart)
        clear_cart_button.pack()

        checkout_button = tk.Button(self.root, text="Checkout", command=self.checkout)
        checkout_button.pack()

    def add_to_cart(self, product, price, quantity_entry):
        quantity = int(quantity_entry.get())
        if quantity > 0:
            self.cart.append((product, price, quantity))
            self.cart_label.config(text=f"Cart: {', '.join([f'{p} x{q} - Rs. {p*q}' for p, _, q in self.cart])}")

    def clear_cart(self):
        self.cart = []
        self.cart_label.config(text="Cart: ")

    def checkout(self):
        total_cost = sum(price * quantity for _, price, quantity in self.cart)
        checkout_message = f"Total Cost: Rs. {total_cost}"
        self.cart_label.config(text=checkout_message)

root = tk.Tk()
app = StoreGUI(root)
root.mainloop()
