from __future__ import annotations
from abc import ABC, abstractmethod

class Builder(ABC):
    def reset(self) -> None: pass
    def buildStepA(self) -> None: pass
    def buildStepB(self) -> None: pass


class ConcreteBuilder1(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.product = Product1()

    def buildStepA(self) -> None:
        self._product.add("PartA-11")

    def buildStepB(self) -> None:
        self._product.add("PartB-11")

    def getResult(self) -> None:
        return self.product



class ConcreteBuilder2(Builder):
    def __init__(self) -> None:
        self.reset()

    def reset(self):
        self.product = Product1()

    def buildStepA(self) -> None:
        self._product.add("PartA-11")

    def buildStepB(self) -> None:
        self._product.add("PartB-11")



class Product1():
    def __init__(self):
        self.parts = []

    def add(self, part: Any):
        self.parts.append(part)

    def list_parts(self):
        print(f"Product parts are : {', '.join((self.parts))}", end="")


##################################

