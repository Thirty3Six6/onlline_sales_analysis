if __name__ == "__main__":
    manager = ProductManager()
    manager.add_products(Product("Laptop", 100, 5))
    manager.add_products(Product("Mouse", 10, 20))
    manager.show_all_product()
    manager.total_value()
    
    cart= ShoppingCart()
    
    cart.add_to_cart(Product("Laptop", 100, 5), 2)
    cart.add_to_cart(Product("Mouse", 10, 20), 5)
    cart.add_to_cart(Product("Laptop", 100, 5), 3)
    cart.show_cart()
    
    cart.calculate_total()