class product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

   
class ShoppingCart:
    def __init__(self):
        self.items=[]

    def add_items(self,item):
        self.items.append(item)
        print(f"Item {item.name} added to the cart")

    def remove_items(self,item):
        for item in self.items:
            if item.lower()==self.items.lower():
                self.items.remove(item)
            else:
                print(f"Item {item.name} not found in the cart.")

    def display_items(self):

        if item not in self.items:
            print(f"Item {item.name} not found in the cart.")
            return

        print("Items in the cart:")
        for item in self.items:
            print(f"- {item.name} - ₹{item.price}")

    def calculate_total(self):
        total=0
        for
