

# constructor

class Point:

    # with "init" method we initialize our object and we
    # ...refer this method as a "constructor/create an object"
    # setting "x" attribute of current object to the "x" argument
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# create a new "point" object
point = Point(10, 20)

# we set "x" attribute to "point" object
print(point.x)
print(point.y)


# exercise: a "person" class with "name" attribute and "talk" method




class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person("Tom")
# print(person.name)
person.talk()

person2 = Person("Jerry")
person2.talk()










