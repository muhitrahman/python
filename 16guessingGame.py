# create three variables and assigning values to them
secret_number = 9
guess = None
guess_start = 0
guess_limit = 3

# comparision one value with another
# asking/printing for user input
# incrementing          start point every time

while guess_start < guess_limit:
    guess = int(input("guess: "))
    guess_start += 1

    # here if statement to check if the user make the right guess
    #     if guess is right, print message
    #     end if statement inside while block

    if guess == secret_number:
        print("you win")
        break

    # if user don't guess it right, while loop continue and print
    # /failed message after 3 guess

else:
    print("you failed !")
