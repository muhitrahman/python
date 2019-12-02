# inheritance is a mechanism for re-using code
# inheritance stop duplicating same code everywhere


class Mammal:
    def animal_planet(self):
        print("they are mammal")


class Dog(Mammal):
    def bark(self):
        print("birk")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.animal_planet()
dog1.bark()
