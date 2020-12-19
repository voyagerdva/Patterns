# coding: utf-8
""" Типы строя """

class Government:
    """ Само правительство """

    culture = ""
    def __str__(self) -> str:
        return self.culture.__str__()

    def set_culture(self):
        """ Задать строй правительству: это и есть наш ФМ """
        raise AttributeError('Raise: !!! Not Implemented Culture !!!')
    
    
class GovernmentDemocracy(Government):
    def __str__(self) -> str:
        return 'Democracy'
        
class GovernmentDictatorship(Government):
    def __str__(self) -> str:
        return 'Dictatorship'

goverDemo = GovernmentDemocracy()
print(str(goverDemo))

goverDict = GovernmentDictatorship()
print(str(goverDict))
