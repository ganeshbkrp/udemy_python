answer = 5
print("Please guess no. between 1 and 10: ")

guess = int(input())

if guess == answer:
    print("You've guessed it correct the first time")
else:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("You've guessed it correct this time")
    else:
        print("You've got it wrong again")




# if guess < answer:
#    print("Please guess higher")
#    guess = int(input())
#   if guess == answer:
#        print("You have guessed correctly")
#   else:
#        print("Sorry, You have not guessed correctly")
# elif guess > answer:
#    print("Please guess lower")
#    guess = int(input())
#    if guess == answer:
#        print("You have guessed correctly")
#   else:
#        print("Sorry you have not guessed correctly")
#else:
#    print("You have guessed it correct the first time")


