
# 2 type conversion
# 3 if else
# 4 logical operator
# 5 comparision operator

import math

while True:
    try:
        weight = float(input("your weight: "))#user input with variables
        unit = input("(K/k)g or (L/l)bs: ")

    except ValueError:
        print("empty value")
        continue


if unit.upper() == "L":#if statement with upper method
    converted = weight * 1.5#if condition is true we get weight
    print(f"you are {converted} pounds")#fromated string print the weight

elif unit.upper() == "K":
    converted = weight / 1.5
    print(f"you are {converted} kg")



















