# a = 10
# if a > 11:
#     print("Yoo momo")

# else:
#     print("No momo")

# is_male = True# If the boolean value is False it gives no output
# if is_male:
#   print("you are a male")

# user_age = int(input("Enter you age: "))

# if user_age >= 18:
#     print("You can vote")
# else:
#     print("You can't vote")
# is_male = False
# is_tall = True

# if is_male and is_tall:# checks user is male and tall if condition becomes True it gets print out
#     print("You are a tall male")
# elif is_male or not (is_tall):#Checks user is male but not tall if condition matches It gets print
#     print("You/sandy are not a tall man")
# elif not (is_male) and is_tall:#check user is not male but tall if condition matches it gets printed
#     print("You are not male but tall")#Condition matches so this gets printed
# Note: and is a logical operator  , both conditions needs to be True to be printed , If one is False & another is True it doesn't prints | False and False never prints
# or is the opposite of and operator    at least one condition has to be True  | False or False never prints
# else:
#     print("You are neither male nor tall")

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
num3 = int(input("Enter the number 3: "))


def max_num(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(num1, num2, num3))
