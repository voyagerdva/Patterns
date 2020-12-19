class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None
        
    def setBody(self, body):
        self.__body = body
        
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)
        
    def setEngine(self, engine):
        self.__engine = engine
        
    def specification(self):
        print("body: %s" % self.__body.shape)
        print("engine horsepower: %d" % self.__engine.horsepower)
        print("tire size: %d\'" % self.__wheels[0].size)