def momo(
    name, type
):  # we created a function using def and name the function momo and we passed the parameter
    # print("Momo says hi")
    print(
        "Do you love " + name + " She is " + type
    )  # Here we used those two parameters to print out what we want


momo(
    "Nami", "Hot"
)  # we called the momo function and we gave value to the parameters , we can pass any value
momo("Nico", "Cool")  # we called the momo function and we gave value to the parameters


def bee(num):
    return (
        num * num * num
    )  # this have been calculated but discarded/ also after the we use return the function ends instantly
    print("Baddie")  # So this won't be printed/never run


print(
    "Nami is a baddie"
)  # But this will be printed/run because it is outside the function , it can't be effected
result = bee(8)  # return value is stored here
print(result)  
