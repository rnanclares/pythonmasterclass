#
# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}?".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("Please come back in {0} years".format(18-age))

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if gues == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# elif guess > 5:
#     print("Please guess lower.")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time.")

# print("Please guess a number between 1 and 10: ")
# guess = int(input())

# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower.")
#
#     guess = int(input())  # type: int
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly.")
# else:
#     print("You got it first time.")

# age = int(input("How old are you?"))

# # if (age >=16) and (age <=65):
# if 15 < age < 66:
#     print("Have a good day at work")

# if (age < 16) or (age > 65):
#     print("Enjoy your free time")
# else:
#     print("Have a good day at work")
#
# if (some_condition) or (some_weird_function_that_does_stuff()): #Python will check first the condition (first after if)
#     #do something

#false and true ar constants, no boolean data type

# x = "false"
# if x:
#     print("x is true")

### Things that evaluate to False

# print("""False: {0}
# None: {1}
# 0: {2}
# empty list []: {4}
# empty tuple (): {5}
# empty string '': {6}
# empty string "": {7}
# empty mapping {{}}: {8}
# """.format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

# x = input("Please enter some text:")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")
#
# print(not True)
# print(not False)

parrot = "Norwegian Blue"

letter = input("Enter a character:")

if letter in parrot:
    print("Give me an {}, Bob".format(letter))
else:
    print("I don't need that letter")

