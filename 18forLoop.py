


# we use for loop to iterate list of items
# *********************************************

# for item in ["python"]:
# for item in ["tom", "jerry", "john", "jane"]:
# for item in range(5, 10, 2):
#     print(item)

price = [10, 20, 30, 40, 50]
total = 0

# this loop variable "numbers" iterate every time and get
# ...the each value from the above price list
# then add value to "total" variable with
# then get average
# print total and average

for numbers in price:
    total = total + numbers

average = total / len(price)

print(total)
print(average)
















