

import re
import sys


# if temperature is greater than 30
#     it is a hot day
#
# otherwise if it is less than 10
#     it is a cold day
#
# otherwise
#     it is neither cold nor hot

# temperature = 20
#
# if temperature >= 30:
#     print("it is a hot day")
#
# elif temperature <= 10:
#     print("it is a cold day")
#
# else:
#     print("it is neither hot nor cold day")

# if name is less than 3 characters long
#     name must be at least 3 characters
# otherwise if it is more than 50 characters long
#     name can be a maximum of 50 characters
# otherwise
#     name looks good

# name = input("enter your name: ")
#
# while not re.match("[A-Z, a-z]", name):
#     print("only letters")
#     name = input("enter your name")
#
# if len(name) <= 3:
#     print("need more than 3 letters")
#
# elif len(name) >= 5:
#     print("need less than 5 letters")
#
# else:
#     print("good name")

while True:
    try:
        age = int(input("enter your age: "))

    except ValueError:
        print("sorry didn't understand")
        continue

    if age < 0:
        print("must not be negative")
        continue

    if age > 100:
        print("too old to vote")
        continue

    else:
        break

if age < 18:
    print("no vote")

else:
    print("can vote")
