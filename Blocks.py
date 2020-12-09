name = input("Please enter your name:")
age = int(input("How old are you, {0}? ".format(name)))
print(age)

if age < 18:
    print("Come back after {} years". format(18 - age))
elif age == 900:
    print("Sorry Yoda, You are gonna die in Return of the Jedi")
else:
    print("You are eligible to vote")




