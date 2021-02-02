from __future__ import annotations
from abc import ABC, abstractmethod


class English():
    def talk(self):
        print("Eng, hello!")

class Franch():
    def talk(self):
        print("France, bonjour")

############################################
def intro(lang):
    lang.talk()

intro(Franch())
intro(English())
#=============================================

class Parent:
    def action(self):
        print("parent talk")

class Child(Parent):
    def action(self):
        print("Child listen")

c = Child()

c.action()

##############################################
class Salary():
    def __init__(self, pay):
        self.pay = pay

    def getTotal(self):
        return (self.pay * 12)

class Employee():
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def annualSalary(self):
        return "Total: " + str(self.pay.getTotal() + self.bonus)

salary = Salary(100)
employee = Employee(salary, 10)
print(employee.annualSalary())
