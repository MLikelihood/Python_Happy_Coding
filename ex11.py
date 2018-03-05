# def get_integer(help_text="Give me a number: "):
#     return int(input(help_text))
#
#
# age = get_integer("Tell me your age: ")
# school_year = get_integer()
# if age > 15:
#     print("You are over the age of 15")
# print("You are in grade " + str(school_year))


# prime


def checkPrime(num):
    for divisor in range(2, num):
        if num % divisor == 0:
            return False
        else:
            return True


userInput = int(input("Enter a number: "))

if checkPrime(userInput):
    print("It's a Prime Number")
else:
    print("Not a Prime")
