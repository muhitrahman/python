

# ***********************************
# first method
# ***********************************

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     print("x" * x_count)


# ******************************************
# second method
# ****************************************

# create list items
# numbers = [1, 1, 1, 5]
numbers = [5, 2, 5, 2, 2]

# create for loop iteration to generate x
for x_count in numbers:

    # set empty string to add/store data
    output = ""

    # in this inner loop we append each x comming from iteration
    for count in range(x_count):

        # then appending x each time into empty string
        output += "x"

    # print result
    print(output)


















