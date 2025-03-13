class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Price: {self.price}")   
        print(f"Quantity: {self.quantity}")
    
    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
        print(f"Quantity for {self.name} updated to {self.quantity}")

product = Product("Laptop", 100, 5)
product.show_info()
product.update_quantity(10)
product.show_info()