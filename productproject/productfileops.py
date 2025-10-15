import csv

from Product import Product

filename = "products.csv"

def load_products():
   products = []
   try:
       with open(filename, newline='') as csvfile:
           reader = csv.DictReader(csvfile)
           for row in reader:
               product = Product(row['pid'], row['name'],int(row['quantity']), int(row['amount']))
               products.append(product)
   except FileNotFoundError:
        pass
   return products


def save_products(products):
    with open(filename, "w", newline='') as csvfile:
        filednames =['pid','name','quantity','amount']
        writer = csv.DictWriter(csvfile, fieldnames=filednames)
        writer.writeheader()
        for product in products:
            writer.writerow({
                'pid':product.pid,
                'name':product.name,
                'quantity':product.quantity,
                'amount':product.amount
            })
