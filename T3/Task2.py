#class Stack
#Methods:
# 1. shift(): returns one element and removes that element from the list
# 2. unshift(): it should push new element in front
# 3. pop(): returns & removes the last element from the list
# 4. push(): adds new element at the end of the list

stack=[]
class Stack:

    def push(value):
        stack.insert(0,value)
    
    def pop():
        return stack.pop(0)
    
    def shift():
        return stack.pop(-1) if len(stack)>1 else stack.pop(0)
    
    def unshift(value):
        stack.insert(len(stack),value)

    def disp():
        for i in stack:
            print(i)

while True:
    print()
    print("1. shift")
    print("2. unshift")
    print("3. pop")
    print("4. push")
    print("5. display")
    print("6. exit")
    try:  
        i= int(input("Enter Choice: "))
        if i==1:
            Stack.shift()
        elif i==2:
            item=int(input("Enter Item: "))
            Stack.unshift(item)
        elif i==3:
            Stack.pop()
        elif i==4:
            item=int(input("Enter Item: "))
            Stack.push(item)
        elif i==5:
            Stack.disp()
        elif i==6:
            break
        else:
            print("Enter valid choice.")
    except Exception as E:
        print("Enter valid choice.", E)