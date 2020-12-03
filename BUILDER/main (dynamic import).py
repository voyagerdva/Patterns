from importlib import import_module
import Modules.Director as dr

def main():
    director = dr.Director()
    brandList = ["Jeep", "Mersedes", "Subaru"]

    for brand in brandList:
        print("\n", brand)
        module = __import__(brand)
        builder = getattr(module, brand + "Builder")
        instance = builder()
        director.setBuilder(instance)
        car = director.getCar()
        car.specification()
        
if __name__ == "__main__":
    main()
    

        
        