# Inheritance imporves the code reusability
# Parent has no access to the child class
# Child class can override the attributes or methods through method overriding
# To invoke the parent class in child class, super keyword is used

class A:
    def process(self):
        print("A process")

class B:
    def process(self):
        print("B process")

class C(B,A):
    pass

class D(A,B):
    pass

o1=C()
o1.process()
print(C.mro())
o2=D()
o2.process()
print(D.mro())

# Method resolution Order based on C3 linearization algorithm starting from Python3
# Algorithm defines the MRO of any class as the sum of ...
# The merge is defined by following steps:
# Step1: Take head of the list
# Step2: If the head is not the tail of any other list, then add it to the linearization of C and remove it from the list 
# otherwise look the head of the other list and take it on the base of above condition
# Step3: Repeat the operation until all classes are removed.