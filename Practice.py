# num1 = input("Enter the first number: ")
# num2 = input("Enter the second number: ")
# print(int(num1) + int(num2))
# print(int(num1) * int(num2))
# print(int(num1) - int(num2))
# print(int(num1) / int(num2))

# result =int(num1+num2)# so first the string does the concatenation then it turn it to int so no addition is between

# num = int(input("Enter the number: "))


# print(pow(num, 2))
# print(pow(num, 3))

# nubr = int(input("Enter the number: "))

# if nubr > 0:
#     print(f"{nubr} is positive number")
# elif nubr < 0:
#     print(f"{nubr} is negative number")
# else:
#     print("Zero")

# given_number = int(input("enter the number: "))

# if given_number % 2 == 0:
#     print(f"{given_number} given number is even")
# else:
#     print(f"{given_number} given number is odd")

# num1=int(input("Enter the first number: "))
# num2=int(input("Enter the second number: "))

# if num1 > num2 :
#   print(f"{num1} is greater one")

# else:
#   print(f"{num2} is greater one.")

# marks = int(input("Enter the marks: "))

# if marks >= 65:
#     print(f"Congrats you have passed the exam by {marks} and you grade is B+")
# elif marks >= 50:  # we can add more like this for other marks
#     print(f"Congrats you have passed the exam by {marks} and you grade is B")
# elif marks >= 40:
#     print(f"Congrats you have passed the exam by {marks}")
# else:
#     print(f"You have fail with {marks}")

# user_name = (input("Enter the name: "))
# length=len(user_name)

# if length > 5:
#     print(f"{user_name} length greater than 5 ")
# else:
#     print(f"{user_name} length is not greater than 5")

# word ="level"
# palindrome=word[::-1]
# print(palindrome)
word = input("Enter the words: ")

if word[::-1] == word:
    print(f"{word}  is palindrome word ")
else:
    print(f"{word} is not a palindrome word ")
