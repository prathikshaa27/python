#zerodivisionerror
try:
    input_number = int(input("Enter a number:"))
    to_divide= 100/input_number
    print("Divison:",to_divide)
except ZeroDivisionError:
    print("The number cannot be divided by zero")
finally:
    print("It will be executed whether the exception occurs or not")

#Type error
try:
    new_details ="prathi"+22
except TypeError as e:
    print("Type error",e)
    
#value error
try:
    new_number= int("prathi")
except ValueError as e:
    print("ValueError",e)

#index error - out of range
try:
    new_list = [1,2,3]
    print(new_list[3])
except IndexError as e:
    print("Index Error",e)

#key error
try:
    new_dict={
        "Name":"Prathi",
        "Age":22
}
    print(new_dict["color"])
except KeyError as e:
    print("KeyError",e)

#Attribute error
try:
    fruits_list =["apple","mango","grapes"]
    print(fruits_list.upper())
except AttributeError as e:
    print("Attribute error",e)

#identation error
try:
    print("hello")     
    print("hai")
except IndentationError as e:
    print("Identation error",e)

#raise statement
def divide_two_numbers(first_number, second_number):
    if second_number==0:
        raise ZeroDivisionError("The number cannot be divided by zero")
    return first_number/second_number
try:
    final_output = divide_two_numbers(7,0)
except ZeroDivisionError as e:
    print("Zero division error:",e)

#user defined exceptions

class UserDefinedError(Exception):
    pass
def divide_two_numbers(first_number, second_number):
    if second_number==0:
        raise ZeroDivisionError("The number cannot be divided by zero")
    return first_number/second_number
try:
    final_output = divide_two_numbers(7,1)
except ZeroDivisionError as e:
    print("Zero division error:",e)