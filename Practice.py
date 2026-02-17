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

# if given_number % 2 == 0: # % it checks the reminder if it give reminder then it checks with the ==0 and print the outcome and if it doesn't given reminder it gives different outcome
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
# word = input("Enter the words: ")

# if word[::-1] == word:# word[ ::-1] means that it will start from the last character  so it start one by one from right to left till the end of character and compare it with the word the user give

#     print(f"{word}  is palindrome word ") #if the word still matches even after reversed then it print this
# else:
#     print(f"{word} is not a palindrome word ") # if the word are not same after the reverse  then it print this

# email=(input("Enter the email: "))

# if "@gmail.com" in email:
#   print("valid email")

# else:
#   print("not a valid email")


# numbers = [20, 50, 30, 40]

# print(max(numbers), " is the largest number")
# print(min(numbers), " is the smallest number")
# print(sum(numbers), " is the total sum of the numbers list")

# n = True
# o = False
# if not n == o and not o == n:
#     print("Hawai")
# else:
#     print("No hawai")

# fruits1 = input("Enter the any Fruits you like: ")
# fruits2 = input("Enter the any Fruits you like: ")
# fruits3 = input("Enter the any Fruits you like: ")
# fruits4 = input("Enter the any Fruits you like: ")
# fruits5 = input("Enter the any Fruits you like: ")

# All_fruits = [fruits1, fruits2, fruits3, fruits4, fruits5]

# print(All_fruits)

# remove_first = input("Enter a fruit to remove: ")
# All_fruits.remove(remove_first)
# print(All_fruits)


nums = [10, 20, 100, 90, 80]
user_number = int(input("Enter the number you want to check: "))
if user_number in nums:
    print(f"{user_number} is in nums ")
else:
    print(f"{user_number} does not exit in nums")
