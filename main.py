if __name__ == "__main__":
    manager = ProductManager()
    manager.add_products(Product("Laptop", 100, 5))
    manager.add_products(Product("Mouse", 10, 20))
    manager.show_all_product()
    manager.total_value()