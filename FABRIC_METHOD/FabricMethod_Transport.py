from __future__ import annotations
from abc import ABC, abstractmethod

class ChooseTransport(ABC):
    def choiceOfTransport(self) -> str: #someOperation()
        transport = self.factory_method()
        result = f"для перемещения {transport.movingBy()}"
        return result

    @abstractmethod
    def factory_method(self): #createProduct()
        pass


class I_want_to_fly(ChooseTransport):
    def factory_method(self) -> ConcreteTransport:
        return GoByAirplane()

class I_want_to_drive(ChooseTransport):
    def factory_method(self) -> ConcreteTransport:
        return GoByTrain()

####################################################################

class ConcreteTransport(ABC):
    @abstractmethod
    def movingBy(self) -> str:
        pass

class GoByAirplane(ConcreteTransport):
    def movingBy(self) -> str:
        return "САМОЛЕТ"


class GoByTrain(ConcreteTransport):
    def movingBy(self) -> str:
        return "ПОЕЗД"

#####################################################################

def client_code(moveMethod: ChooseTransport) -> None:
    print("Клиент: Хотим выбрать", moveMethod.choiceOfTransport(), end="\n")


if __name__ == "__main__":
    client_code(I_want_to_fly())
    client_code(I_want_to_drive())