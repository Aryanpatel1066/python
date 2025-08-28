from abc import ABC,abstractclassmethod


# abstract class

class Car(ABC):
    # abstract method not implementation heare
    def start(self):
        pass
    def stop(self):
        pass

# concreate class 1

class ElectricCar(Car):
    # both are concreate method
    def start(self):
        print("electric vehicals was started")
    def stop(self):
        print("car was stop due to power off...")

# concreact class 2

class PetrolCar(Car):
    # also this concreate method
    def start(self):
        print("petrol car was started ...")
    def stop(self):
        print("car was stop fuel is low")

# now create object for both the class

electicarObj = ElectricCar()
petrolcarObj = PetrolCar()

electicarObj.start()
electicarObj.stop()

petrolcarObj.start()
petrolcarObj.stop()

