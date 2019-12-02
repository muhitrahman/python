

# we use classes to define new type.
# like shopping card.
# shopping card is not a boolean, not a list, or not a dictionaries

class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.move()
print(point1.x)
print(point1.y)











