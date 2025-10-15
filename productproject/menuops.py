import productfileops
from ProductCrud import ProductCrud
from Product import Product
from productfileops import *
def menu():
    pd = ProductCrud()
    products = productfileops.load_products()
    while True:
        print("Welcome to Product Management System ")
        print("1. Add Product")
        print("2. Display Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Search Product")
        print("6. Exit")
        choice = input("Enter choice: ")
        try:
            if choice == "1":
                 pid = int(input("Enter Product ID: "))
                 name = input("Enter Product Name: ")
                 quantity = int(input("Enter Product Quantity: "))
                 amount = int(input("Enter Product Amount: "))
                 product = Product(pid, name, quantity, amount)
                 pd.add_product(products,product)

            if choice == "2":
                pd.display_products(products)

            if choice == "3":
                pid = input("Enter Product ID: ")
                pd.update_product(products,pid)

            if choice == "4":
                pid = input("Enter Product ID: ")
                isDeleted = pd.remove_product(products,pid)
                if isDeleted:
                    print("Product Deleted")
                else:
                    print("Product Not Found")

            if choice == "5":
                name = input("Enter Product Name: ")
                data = pd.search_product(products,name)
                if data:
                    print("Product Found: " , data)
                else:
                    print("Product Not Found")

            if choice == "6":
                break
        except Exception as e:
            print(e)

menu()

