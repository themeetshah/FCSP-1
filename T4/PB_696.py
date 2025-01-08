from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Salary: {self.salary}"
    
    def print_details(self):
        print(self.get_details())

    def getSalary(self):
        return self.salary
    
    @abstractmethod
    def emp_id():
        pass

class Perks:
    def __init__(self,salary):
        self.DA = 0.35*salary
        self.HRA = 0.17*salary
        self.PF = 0.12*salary

    def perks(self):
        return self.DA+self.HRA-self.PF
    
    def getDA(self):
        return self.DA
    
    def getHRA(self):
        return self.HRA
    
    def getPF(self):
        return self.PF

class NetSalary(Employee,Perks):
    def __init__(self, id, name, salary):
        Employee.__init__(self,id, name, salary)
        Perks.__init__(self,salary)
    
    def total_salary(self):
        return self.salary+self.perks()
    
    def final_print(self):
        print(f"Empoyee ID:",self.id)
        print(f"Employee Name:",self.name)
        print(f"Employee Basic Salary:",self.salary)
        print(f"DA:",self.getDA())
        print(f"HRA:",self.getHRA())
        print(f"PF:",self.getPF())
        print(f"Total Salary: {self.total_salary()}")

    def emp_id(self):
        return self.id

emp1=NetSalary(1,"John",25000)
emp1.final_print()