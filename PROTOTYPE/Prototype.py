import copy

class Prototype:
    _type = None
    _value = None
    
    def clone(self):
        pass
    
    def getType(self):
        return self._type
    
    def getValue(self):
        return self._value
    
class Type1(Prototype):
    def __init__(self, numvber):
        self._type = "Type1"
        self._value
    