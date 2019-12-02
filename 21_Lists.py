

names = ["tom", "jerry", "jhon", "jane"]
print(names)

# create random list
numbers = [10, 20, 99, 30, 40]

# create a variable to store maximum number
maximum = numbers[0]

# for loop
for number in numbers:

    # check if number is greater than max
    if number > maximum:

        # then we need to reset maximum to this number
        maximum = number

# result
print(maximum)



