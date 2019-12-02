
# generating random values


import random


# for i in range(3):
#     print(random.random())

# for i in range(3):
#     print(random.randint(10, 20))

# members = ["tom", "jerry", "john", "jane"]
# leader = random.choice(members)
# print(leader)

# Exercise
class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)

        return first, second


dice = Dice()
print(dice.roll())

# create Dice class
# create roll function
# crate two random number from i to 6
# return those two random number
# create Dice class object
# print object + function
