class Car:
    def __init__(self,name,color):
        self.name =name
        self.color=color
    def sound(self):
        print(f"The {self.name} is {self.color} in color and it produces a huge sound")
car1=Car("Hyundai","Blue")
car1.color="pink" #changing the value of the object
print(car1.name)
print(car1.color)
car1.sound()

class BankAccount:
    def __init__(self,account_holder,account_number):
        self.account_holder = account_holder
        self.account_number=account_number
    def check_balance(self):
        print(f"Account holder:{self.account_holder}, Account Number:{self.account_number}, Your current balance is 10,000")
    
person1=BankAccount("Prathi", 26636466)
person2=BankAccount("Mike", 245366371)
person1.check_balance()
person2.check_balance()

class Employee:
    def __init__(self,name,domain):
        self.name = name
        self.domain=domain

    def assign_task(self):
        print(f"Name :{self.name}, Domain:{self.domain}, You can do the coding part for the application")
employee1= Employee("Jack", "Development")
employee1.assign_task()