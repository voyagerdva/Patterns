import Modules.Builder as bld
import Modules.Details as dtl

class MersedesBuilder(bld.Builder):
    def getWheel(self):
        wheel = dtl.Wheel()
        wheel.size = 55
        return wheel
    
    def getEngine(self):
        engine = dtl.Engine()
        engine.horsepower = 6211
        return engine
    
    def getBody(self):
        body = dtl.Body()
        body.shape = "Sedan"
        return body