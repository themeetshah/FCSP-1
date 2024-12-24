#WAP to stimulate Dominos app
#class Pizza that calculates the prize of a pizza based on size, toppings and cheese
#price dependencies:
#   size: small(60), medium(100), large(200)
#   toppings: onion(20), corn(20), capsicum(20), olives(50), mushroom(50)
#   cheese slice: 50 each
#class Order that allows user to place multiple orders. the class should ask user to customize each pizza and calculate total bill
#write functionality to print order details along with total bill

class Pizza:
    def __init__(self, size, toppings, cheese, cost):
        self.size = size
        self.toppings = toppings
        self.cheese = cheese
        self.cost=cost

class Order:
    sizee={"small":60, "medium":100, "large":200}
    toppingss={"onion":20, "corn":20, "capsicum":20, "olives":50, "mushroom":50}
    cost=0

    def calc(self,size,toppings,cheese):
        if size in Order.sizee:
            self.cost+=Order.sizee[size]
        if toppings in Order.toppingss:
            self.cost+=Order.toppingss[toppings]
        if cheese:
            self.cost+=50*cheese
        return self.cost

orders=[]
while True:
    try:
        print("\n1. Place Order")
        print("2. View Orders")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            size = input("Enter size (small/medium/large): ").lower()
            if size not in ["small","medium","large"]:
                raise Exception("Invalid choice. Please try again.")
            toppings = input("Enter toppings (onion/corn/capsicum/olives/mushroom): ").lower()
            if toppings not in ["onion","corn","capsicum","olives","mushroom"]:
                raise Exception("Invalid choice. Please try again.")
            cheese = int(input("Enter number of cheese slices: "))
            cost= Order.calc(Order, size, toppings,cheese)
            orders.append(Pizza(size, toppings, cheese, cost))
            print(f"Order placed successfully. Total bill: {cost}")
        elif choice == 2:
            if len(orders)==0:
                print("No orders placed yet.")
            else:
                print("\nOrders:")
                print("====================================")
                for i in range(len(orders)):
                    print()
                    print(f"Order {i+1}:")
                    print(f"Size: {orders[i].size}")
                    print(f"Toppings: {orders[i].toppings}")
                    print(f"Cheese Slices: {orders[i].cheese}")
                    print(f"Total Bill: {orders[i].cost}")
                    print()
                    print("====================================")
        elif choice == 3:
            break
    except:
        print("Invalid choice. Please try again.")