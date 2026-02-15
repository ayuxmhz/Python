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

num1 = int(input("Enter the number 1: "))  # takes input from the user also take int
num2 = int(input("Enter the number 2: "))  # takes input from the user also take int
num3 = int(input("Enter the number 3: "))  # takes input from the user also take int


def max_num(
    num1, num2, num3
):  # we create a function and name it max_num , where we will be passing  three numbers to check the largest number

    if num1 >= num2 and num1 >= num3:  # checks num1 is larger than num2 nad num3
        # print(
        #     f"Num1 is largest number and the number is:{num1}"
        # )  # instead of printing at the last we printed here | it only gets printed out if the condition is True
        return num1
    elif num2 >= num1 and num2 >= num3:  # checks num2 is larger than num1 and num3
        # print(
        #     f"Num2 is the largest number and the number is:{num2} "
        # )  # it only gets printed out if the condition is True
        return num2
    else:  # This run if both num1 and num2 are smaller than num3
        # print(
        #     f"Num3 is largest Number and the number is :{num3}"
        # )  # it only gets printed out if the condition is True
        return num3


# print(max_num(num1, num2, num3))
Largest = max_num(num1, num2, num3)#here we just created a variable where max_num is stored 
print(f"The largest number is: {Largest}")


# number = 20
# print(f"Sum: {number +number}")
# print(f"Type: {type(number)}")