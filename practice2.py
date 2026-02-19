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

# secret_number = 99
# user_number = 0
# tries = 0
# total_tires = 3
# out_of_tries = False

# while user_number != secret_number and not (out_of_tries):
#     if tries < total_tires:
#         user_number = int(input("Enter the number: "))
#         tries += 1
#     else:
#         out_of_tries = True

# if out_of_tries:
#     print("Sorry!! You are out of tries, Try next time goodbye to you money")
# else:
#     print("Congrats you have guess the winning number")


# Task 6
# mul_num = int(input("Enter the number you want multiplication of: "))
# num = 1

# while 10 >= num:
#     mul = mul_num * num
#     print(f"{mul_num} x {num}: {mul}")
#     num += 1

# Task 7
# Baddie_list = ["Nami", "Nico Robin", "Boa hancock", "Vivi", "Hinata", "Orihime"]

# for index in range(len(Baddie_list)): # range(lne(Baddie_list)) means loop equal to the length of the list so the length of list is 6  it runs and prints all the name from the list
# print(index,Baddie_list[index])# we are accessing names through index

# simpler one just access the names
# for name in Baddie_list:
#     print(name)

# Task 8
# numbers = [2, 4, 6, 8, 10]
# total = 0

# for num in numbers:
#     total += num
# print(f"The total sum of number:{total}")

# Task 9
find_even = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
]
counts = 0
for even in find_even:
    if even % 2 == 0:
        counts += 1
print(f"There are total {counts} even number in the list ")
    # else:
    #   print(f"{even} is not even number")
