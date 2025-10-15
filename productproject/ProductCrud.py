import Product
import productfileops
from productfileops import *
import productnotfound
class ProductCrud:
    products = []

    def __init__(self):
        self.products = load_products()

    def add_product(self, products, product):
        products.append(product)
        save_products(products)
        print("Product Added successfully")


    def remove_product(self, products, id):

        isFound=False
        for product in products:
            if product.pid == id:
                products.remove(product)
                isFound=True
                break
        if isFound:
            productfileops.save_products(products)
            return True
        else:
            raise productnotfound.ProductNotFound(f"Product not found with {id} id ")



    def display_products(self, products):

        if not products:
            print("No products found in the list")
        else:
            for product in products:
                print(product)


    def search_product(self, products,name):
        temp=None
        for product in products:
            if product.name== name:
                temp = product
                break
        return temp

    def update_product(self, products, id):
        print(id)
        for product in products:
            if product.pid == id:
                product.name = input("Enter product name: ")
                product.quantity = int(input("Enter product quantity: "))
                product.amount = float(input("Enter product price: "))
                save_products(products)
                return
        raise productnotfound.ProductNotFound(f"Product not found with {id} id ")



