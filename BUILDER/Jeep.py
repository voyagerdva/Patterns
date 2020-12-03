import Modules.Builder as bld
import Modules.Details as dtl

class JeepBuilder(bld.Builder):
    def getWheel(self):
        wheel = dtl.Wheel()
        wheel.size = 22
        return wheel
    
    def getEngine(self):
        engine = dtl.Engine()
        engine.horsepower = 400
        return engine
    
    def getBody(self):
        body = dtl.Body()
        body.shape = "SUV"
        return body