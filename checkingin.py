parrot = "Norwegian Blue"

letter = input("Enter a chanracter: ")

if letter in parrot:
    print("{} is in {}". format(letter, parrot))
else:
    print("I don't need that latter")
