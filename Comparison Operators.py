temperature = 35

if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

# Exercise

name = input("Please enter your age: ")

if len(name) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good")