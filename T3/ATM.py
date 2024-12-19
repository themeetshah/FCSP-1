#wap to stimulate Bank ATM
#Menu:
#   1. Create PIN
#   2. Change PIN
#   3. Check Balance
#   4. Withdraw Money
#Methods:
#   1. createPin()
#   2. changePin()
#   3. checkBalance()
#   4. withdrawAmount()

atm=[]
class ATM:
    def createPin():
        pin = input("Enter your new PIN: ")
        self1=ATM.checkPin(pin)
        if self1 is None:
            self1=ATM()
            self1.pin=pin
            self1.balance = float(input("Enter your balance: "))
            atm.append(self1)
            print("PIN created successfully")
        else:
            print("PIN already exists")

    def changePin(opin):
        self1=ATM.checkPin(opin)
        if self1 is not None:
            npin=input("Enter pin: ")
            self1.pin = npin
            print("PIN changed successfully")
        else:
            print("no such user")

    def checkBalance():
        pin=input("Enter pin: ")
        self1=ATM.checkPin(pin)
        if self1 is not None:
            print(self1.balance)
        else:
            print("No such user")
    
    def withdrawAmount():
        pin=input("Enter pin: ")
        self1=ATM.checkPin(pin)
        if self1 is not None :
            amt=float(input("Enter amt: "))
            if amt<self1.balance:
                self1.balance-=amt
                print(self1.balance)
            else:
                print("insufficient balance")
        else:
            print("no such user")

    def checkPin(pin):
        for i in atm:
            if pin==i.pin:
                return i
        else:
            return None
    

while True:
    print()
    print("1. Create Pin")
    print("2. Change Pin")
    print("3. Check balance")
    print("4. Withdraw Money")
    print("5. exit")
    try:  
        i= int(input("Enter Choice: "))
        if i==1:
            ATM.createPin()
        elif i==2:
            pin=input("Enter old pin: ")
            ATM.changePin(pin)
        elif i==3:
            ATM.checkBalance()
        elif i==4:
            ATM.withdrawAmount()
        elif i==5:
            break
        else:
            print("Enter valid choice.")
    except Exception as E:
        print("Enter valid choice.", E)