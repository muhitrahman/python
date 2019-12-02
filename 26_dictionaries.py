
# we use dictionaries when we use key and value to store together

details = {
    "name": "tom",
    "age": 30,
    "is_verified": True
}
# details["age"] = 35
# details["year"] = 1980

print(details["name"])
print(details.get("year", "key name is not correct"))

# write 1234 and print string name
phone = input("phone: ")
digits_mapping = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}
output = ""
# we loop the phone string
for character in phone:
    # now access the dictionaries with key and value and
    # ...add it to the empty output string
    output = output + digits_mapping.get(character, "!") + " "
# print the new output string
print(output)
