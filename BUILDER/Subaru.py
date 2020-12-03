import Modules.Builder as bld
import Modules.Details as dtl

class SubaruBuilder(bld.Builder):
    def getWheel(self):
        wheel = dtl.Wheel()
        wheel.size = 111
        return wheel
    
    def getEngine(self):
        engine = dtl.Engine()
        engine.horsepower = 1999
        return engine
    
    def getBody(self):
        body = dtl.Body()
        body.shape = "Universal"
        return body
    
    def getAntenna(self):
        antenna = dtl.Antenna()
        antenna.frequency = "548 MHz"
        return antenna
    
    # def getSpecification(self):
    #     print("body: %s" % self.__body.shape)
    #     print("engine horsepower: %d" % self.__engine.horsepower)
    #     print("tire size: %d\'" % self.__wheels[0].size)
    #     print("antenna frequency: %s" % self.__wheels[0].size)