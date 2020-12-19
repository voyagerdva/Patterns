# coding: utf-8
""" Типы строя """

class Culture:
    """ Культура """
    def __repr__(self):
        return self.__str__
    
class Democracy(Culture):
    def __str__(self) -> str:
        return 'Democracy'
    
class Dictatorship(Culture):
    def __str__(self) -> str:
        return 'Dictatorship'

class Government:
    """ Само правительство """
    culture = ""
    def __str__(self) -> str:
        return self.culture.__str__()

    def __repr__(self):
        return self.culture.__repr__()

    def set_culture(self):
        """ Задать строй правительству: это и есть наш ФМ """
        raise AttributeError('Raise: !!! Not Implemented Culture !!!')
    
class GovernmentA(Government):
    def set_culture(self):
        self.culture = Democracy()
        
class GovernmentB(Government):
    def set_culture(self):
        self.culture = Dictatorship()

goverA = GovernmentA()
goverA.set_culture()
print(str(goverA))

goverB = GovernmentB()
goverB.set_culture()
print(str(goverB))
