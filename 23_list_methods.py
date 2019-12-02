numbers = [5, 2, 2, 7]

# numbers[0] = 99
# numbers.append(10)
# numbers.reverse()
# numbers.sort()
# print(numbers.copy())
# numbers.remove(5)
# numbers.pop()
# print(numbers.index(7))
# print(numbers.count(2))
# print(numbers.index(50))
# print(50 in numbers)
# numbers.clear()

# print(numbers)

# **********************************************

# numbers = list(dict.fromkeys(numbers))
# print(numbers)

duplicate = []
for number in numbers:
    if number not in duplicate:
        duplicate.append(number)

print(duplicate)

# ***********************************************

# numbers2 = numbers.copy()
# numbers.append(10)
# print(numbers2)
