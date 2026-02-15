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
is_male = False
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male or not (is_tall):
    print("You/sandy are not a tall man")
elif not (is_male) and is_tall:
    print("You are not male but tall")
else:
    print("You are neither male nor tall")
