#WAP to stimulate Dominos app
#class Pizza that calculates the prize of a pizza based on size, toppings and cheese
#price dependencies:
#   size: small(60), medium(100), large(200)
#   toppings: onion(20), corn(20), capsicum(20), olives(50), mushroom(50)
#   cheese slice: 50 each
#class Order that allows user to place multiple orders. the class should ask user to customize each pizza and calculate total bill
#write functionality to print order details along with total bill

class Pizza:
    def __init__(self, size, toppings, cheese):
        self.size = size
        self.toppings = toppings
        self.cheese = cheese

class Order:
    def calc(size,toppings,cheese):
        if size == 'small':
            price = 60
        elif size == 'medium':
            price = 100
        elif size == 'large':
            price = 200
        
        