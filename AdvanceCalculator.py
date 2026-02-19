def calculator():  # we created function called calculator
    print("=== Simple Calculator ===")

    num1 = float(
        input("Enter first number: ")
    )  # taking input from user it takes both int = whole number and floating number = 1.0 decimal numbers
    operator = input(
        "Enter operator (+, -, *, /): "
    )  # we are asking user for an operator to perform sum(+), sub(-) , div(/) and mul(*)
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if (
            num2 != 0
        ):  # Handle division by zero | so if the num2 is not equal to 0 it gives the result
            result = num1 / num2
        else:  # only gets it printed if num2 is zero
            return "Error: Cannot divide by zero!"
    else:  # if user gives invalid operator this runs
        return "Error: Invalid operator"

    return f"{num1} {operator} {num2} = {result}"  # using f string so it would look clean example if user gives 4 for num1 and (*) for operator and 2 for num2 then it could look like 4 * 2 = 8 which is result


# # Let user do multiple calculations
while True:
    print(calculator())
    while True:
        # print(calculator())  # we called the function=calculator  inside the while loop so that user can choose to calculate again or not
        again = input("\nCalculate again? (y/n):").lower()  # asking if user wants to calculate again or not by choosing y/n
        if (again == "y"):  # .lower() function lowers anything user give example "Y" gonna be -> "y"
            break
        elif again == "n":
            print("Goodbye!")
            exit()
            # break  # If we haven't put break here it could loop again because the condition here is always True | so we put break if the user give n then it breaks the loop right way
        else:
            print("Invalid input! Please enter 'y' or 'n'.")
