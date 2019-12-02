
# dictionaries can map one character into another character with "split method"

# input string
message = input(">")
# split method
words = message.split(" ")
# dictionaries with key and value
emoji = {
    ":)": "😊",
    ":(": "☹",
}
# output variables
output = ""
# loop the split method variable
for character in words:
    # get dictionaries with key and value and add it to
    # output string
    output = output + emoji.get(character, character) + " "
# print new output variables
print(output)







