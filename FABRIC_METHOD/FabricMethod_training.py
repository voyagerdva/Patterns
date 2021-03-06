from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    def someOperation(self):
        return self.createProduct().doStuff()

    @abstractmethod
    def createProduct(self):
        pass


class ConcreteCreatorA(Creator):
    def createProduct(self):
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def createProduct(self):
        return ConcreteProductB()

######################################################

class Product():
    @abstractmethod
    def doStuff(self):
        pass

class ConcreteProductA(Product):
    def doStuff(self):
        print("make ConcreteProductA")

class ConcreteProductB(Product):
    def doStuff(self):
        print("make ConcreteProductB")

######################################################

def application(creator: Creator):
    creator.someOperation()

application(ConcreteCreatorA())
application(ConcreteCreatorB())


