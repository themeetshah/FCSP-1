#wap to create StoreManagementSystem
#class Store
#initialize: ItemCode, Prize 
#method:    
#       getData(): get ItemCode and price from user
#       displayData(): Display ItemCode and price
#       printBill(): generate and print bill based on itemCode, quantity purchased
#               BILL
#========================================
#   ItemCode    Price     Qty.    TPrice

items={}
class Store:
    itemCode=0
    price=0
    quantity=0
    totalPrice=0

    def __init__(self,itemCode,price,qty):
        self.itemCode=itemCode
        self.price=price
        self.quantity=qty
        items[itemCode]=self

    def getData(itemCode):
        if items.get(itemCode,0)!=0:
            print("ItemCode: ",itemCode)
            print("Price: ",items[itemCode].price)
            print("Quantity: ",items[itemCode].quantity)
        else:
            print("No such item found")
    
    def displayData():
        for i in items:
            print(f"ItemCode: {items[i].itemCode}, Price: {items[i].price}")
    
    def printBill():
        print("=======================================================================")
        print("BILL".rjust(35))
        print("=======================================================================")
        print(f"  Item Code".ljust(20)+"Price".ljust(20)+"Quantity".ljust(20)+"Total")
        total=0
        for i in items:
            tprice=items[i].price*items[i].quantity
            total+=tprice
            print(f"    {items[i].itemCode}".ljust(20)+f"{items[i].price}".ljust(20)+f"{items[i].quantity}".ljust(20)+f"{tprice}")
        print(f"----------------------------------------------------------------------")
        print("Grand Total: "+f"{tprice}".rjust(53))

while True:
    print()
    print("1. Give Data")
    print("2. Get Data")
    print("3. Display Data")
    print("4. Print Bill")
    print("5. Exit")
    try:  
        i= int(input("Enter Choice: "))
        if i==1:
            itemCode=int(input("Enter ItemCode: "))
            price=float(input("Enter Price: "))
            quantity=int(input("Enter Quantity: "))
            Store(itemCode,price,quantity)
        elif i==2:
            itemCode=int(input("Enter ItemCode: "))
            Store.getData(itemCode)
        elif i==3:
            Store.displayData()
        elif i==4:
            Store.printBill()
        elif i==5:
            break
        else:
            print("Enter valid choice.")
    except Exception as E:
        print("Enter valid choice.", E.args)