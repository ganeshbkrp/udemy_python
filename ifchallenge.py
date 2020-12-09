name = input("What is your name: ")
age = int(input("What is your age: "))

if 18 <= age < 30:
    print("Welcome to the club 18-30 holidays {0}".format(name))
else:
    print("You are not part of the cool club")
