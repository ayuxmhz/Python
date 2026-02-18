# Task 1
# num = 1
# user_number = int(input("Enter the number: "))

# while num <= user_number:
#     print(num)
#     num += 1

# Task 2
# number = 1
# user_num = int(input("Enter the number: "))

# while user_num >= number:
#     print(user_num)
#     user_num -= 1

# Task 3
# ur_number = int(input("Enter the number: "))
# num = 1
# total_sum = 0

# while num <= ur_number:

#     total_sum += num
#     num += 1

# print(f" The sum from 1 to {ur_number} is: {total_sum}")

# Task 4
# password = "python123"
# user_password = " "


# while user_password != password:
#     user_password = input("Enter the password: ")
#     if user_password == password:
#         print("Access Granted!")
#     else:
#         print("Access denied!,Try again!! \n")


# Task 5

secret_number = 99
user_number = " "
tries = 0
total_tires = 3
out_of_tries = False

while user_number != secret_number and not (out_of_tries):
    if tries < total_tires:
        user_number = int(input("Enter the number: "))
        tries += 1
    else:
        out_of_tries = True

if out_of_tries:
    print("Sorry!! You are out of tries, Try next time goodbye to you money")
else:
    print("Congrats you have guess the winning number")
