#public
class Vehicle:
    def __init__(self,name,size):
        self.name = name
        self.size=size
    def sound(self):
        print("It makes a large noise")
car = Vehicle("Toyato", "Large")
bike = Vehicle("Honda","Medium")
print(car.name)
print(car.size)
print(bike.name)
print(bike.size)
car.sound()

#protected 

class Person:
    _name = "prathi"
    _aadharNumber = 53627277872
    _pancard = "HAVPP1256"
class Details(Person):
        def __init__(self):
         print(self._name)
         print(self._aadharNumber)
         print(self._pancard)

person1 = Details()

#directly accessing the protected member
#print(person1.name)

#private

class Hospital:
    __no_of_patients = 0
    __available_medicine =0
    def __init__(self):
        self.__no_of_patients= 100
        self.__available_medicine= 550
        print(self.__no_of_patients)
        print(self.__available_medicine)
details = Hospital()   
 #accessing outside of the class
print(details.__available_medicine)

