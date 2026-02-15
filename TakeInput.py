# name = input("Enter you name: ")
# age = input("Enter a number: ")
# print("Hello " + name + " How are you?")
# print("Your age is " + age + "!!")

nub1 = input("Enter a number: ")
nub2 = input("Enter another number: ")
result = float(nub1) + float(
    nub2
)  # int function  is a full number, we can't add int and float together using int function so we use float function now we can add floatnumber 4.5 and int number 5 = 9.5
print(result)

# print(type(10))
# print(type(90.0))
x = 90.5
if x.is_integer():
    x = int(x)

print(x)  # 90

y = 90.5
if y.is_integer():
    y = int(y)

print(y)  # 90.5
