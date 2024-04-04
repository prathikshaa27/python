# Basic
first_number = 200
second_number = 200
if (first_number == second_number):
    print('Equal')
else:
    print("Not equal")
if (first_number > second_number):
    print("Passed")
else:
    print("Failed")

eligible_age = 18
if (eligible_age):
    print("Eligible to vote")
else:
    print("Not eligible to vote")

new_number = -18
if (new_number > 0):
    print("Positive")
elif (new_number == 0):
    print("Zero")
else:
    print("Negative")

# using and
third_number = 8
fourth_number = 7
if (third_number % 2 == 0) and (fourth_number % 2 == 0):
    print("Even")
else:
    print("Odd")

# using or
fifth_number = 18
if (fifth_number % 3 == 0) or (fifth_number % 5 == 0):
    print("It is divsible by both")
else:
    print("It is not divisible by 3 and 5")

# using not
smaller_number = 12
larger_number = 17
if (not smaller_number > larger_number):
    print("it is not greater")
else:
    print("condition not satisfied")

# nested if
some_number = 75
if (some_number > 50):
    print("It is greater than 50")
    if (some_number > 70):
        print("It is greater than 70")
    else:
        print("It is greater than 70")
# pass
a = 200
b = 200
if (a > b):
    pass

package_weigth = 3
if (package_weigth <= 2):
    print("The cost is $5")
elif (package_weigth > 2 and package_weigth <= 5):
    print("The cost is $4")
elif (package_weigth > 5 and package_weigth <= 10):
    print("The cost is $3")
else:
    print("The cost is $2")
