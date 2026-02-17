# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print(num1 + num2)
# print(num1 * num2)
# print(num1 - num2)
# print(num1 / num2)

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

# user_name = (input("Enter the name: "))# we ask a name from the user
# length=len(user_name)# it is to check the length of name user gave

# if length > 5:#to check user name is greater than 5 or not
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

# email=(input("Enter the email: "))#we ask user to write down email

# if "@gmail.com" in email: # checks if the email the user gave have @gmail.com or not  and the keyword we use to check that is "in"  keyword
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

# fruits1 = input("Enter the any Fruits you like: ")# asking user from the fruits they want to add in the all fruits list
# fruits2 = input("Enter the any Fruits you like: ")# asking user from the fruits they want to add in the all fruits list
# fruits3 = input("Enter the any Fruits you like: ")# asking user from the fruits they want to add in the all fruits list
# fruits4 = input("Enter the any Fruits you like: ")# asking user from the fruits they want to add in the all fruits list
# fruits5 = input("Enter the any Fruits you like: ")# asking user from the fruits they want to add in the all fruits list

# All_fruits = [fruits1, fruits2, fruits3, fruits4, fruits5] # putting the fruits the user gave in the all fruits list

# print(All_fruits)#prints all the fruits from the all fruits list

# remove_first = input("Enter a fruit to remove: ")# we are asking fruit that user want to remove from the all fruits list
# All_fruits.remove(remove_first)#removes the fruit the user gave
# print(All_fruits)#updated all fruits list


# nums = [10, 20, 100, 90, 80]
# user_number = int(input("Enter the number you want to check: "))
# if user_number in nums:
#     print(f"{user_number} is in nums ")
# else:
#     print(f"{user_number} does not exit in nums")


# user_info = {"Name": "Zoro", "Age": 24, "city": "Uptown"}
# # prints one by one value |
# print(user_info["Name"])
# print(user_info["Age"])
# print(user_info["city"])
# print(user_info.values())# prints all the values from the dictionary=user_info

user_dict = {
    "name": "Nami",
    "age": 21,
}
# user_key=input("Enter the keys: ")
# user_value=input("Enter the value: ")

# user_dict.updatt({user_key:user_value})
# print(user_dict)

check_dict = input("enter the key you want to check: ")

print(user_dict.get(check_dict))


if user_dict.get(check_dict) is not None:
    print(f"{check_dict} key is in the user_dictionary")
else:
    print(f"{check_dict} key does not exit in the user_dictionary")
