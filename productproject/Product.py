class Product:
       def __init__(self, pid, name, quantity,amount):
            self.pid=pid
            self.quantity=quantity
            self.name=name
            self.amount=amount
       def __str__(self):
            return f"ID = {self.pid}, Name = {self.name}, Quantity = {self.quantity}, Price = {self.amount}"

