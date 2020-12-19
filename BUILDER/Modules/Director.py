import Modules.Car as cr

class Director:
    __builder = None
    
    def setBuilder(self, builder):
        self.__builder = builder
        
    def getCar(self):
        car = cr.Car()
        
        # сперва идет кузов
        body = self.__builder.getBody()
        car.setBody(body)

        # затем двигатель
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # затем 4 колеса
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel) 
            i += 1
            
        return car