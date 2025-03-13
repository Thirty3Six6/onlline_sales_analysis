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

#dodano