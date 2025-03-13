class ProductManager:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products = [product]
    
    def add_products(self, product):
        self.products.append(product)
        print(f"Product {product.name} added to the list")
   
    def show_all_product(self):
        self.products.append(product)
        for product in self.products:
            product.show_info()
    
    def total_value(self):
        total = sum([product.price * product.quantity for product in self.products])
        print(f"Total value of all products: {total}")    
        
        
    def remove_product_by_name(self,product_name):
        self.products = [product for product in self.products if product.name != product_name]
        print(f"Product {product_name} removed from the list")

class Cart:
    def __init__(self):
        self.cart_items = []
        
    def add_to_cart(self, product, quantity):
        for item in self.cart_items:
            if item.product == product:
                item.quantity += quantity
                print(f"Added more quantity of {product.name} to the cart, new quantity: {item.quantity}")
                return    
   
    def calculate_total(self):
        total = sum([item.product.price * item.quantity for item in self.cart_items])
        print(f"Total value of all products in the cart: {total}")    
        
    def show_cart(self):
        if not self.cart_items:
            print("Cart is empty")
        else:
            for item in self.cart_items:
                print(f"Product: {item.product.name}, Quantity: {item.quantity}")