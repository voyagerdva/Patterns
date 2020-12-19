import Modules.Director as dr
import Jeep as jp
import Mersedes as mrs
import Subaru as sbr

def main():
    director = dr.Director()
    
    # создание джипа:
    print("\n", "Jeep")
    jeepBuilder = jp.JeepBuilder()  # создание экземпляра класса
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()

    # создание мерседеса:
    print("\n", "Mersedes")
    mersedesBuilder = mrs.MersedesBuilder()  # создание экземпляра класса
    director.setBuilder(mersedesBuilder)
    mersedes = director.getCar()
    mersedes.specification()

    # создание субару:
    print("\n", "Subaru")
    subaruBuilder = sbr.SubaruBuilder()  # создание экземпляра класса
    director.setBuilder(subaruBuilder)
    subaru = director.getCar()
    subaru.specification()

if __name__ == "__main__":
    main()
    

        
        