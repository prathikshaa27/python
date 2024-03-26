text = "prathi"
print(text)
print(len(text))

#multiline strings

text = "" " Hello this is prathi iam from cbe . I work in aspire systems as a fresher. I belong to Lamp"""
print(text)

#slicing

slicing_string = "Aspire systems"
print(slicing_string[1:4])
print(slicing_string[:14])
print(slicing_string[7:])
print(slicing_string[-1])

#modifying strings
text = "prathi"
print(text.upper())
print(text.lower())

#strip - removes whitespace
text=" Python Language "
print(text)
print(text.strip())

#replace
replace_string = "I went ,to a shop"
print(replace_string.replace("I","You"))

#split
print(replace_string.split(" ,"))

#concate strings 

concate_string1= "Hello"
concate_string2 = "This is prathi"
print(concate_string1+" "+concate_string2)

#formatting
fruits_price = 45
total_cost ="The total amount for the fruit is {} Rs"
print(total_cost.format(fruits_price))

#string methods

my_name= "prathikshaa27"
print(my_name.capitalize())
print(my_name.casefold())
to_centeralise = my_name.center(50)
print(to_centeralise)
print(my_name.count('a'))
print(my_name.endswith('a'))
print(my_name.find('t'))
print(my_name.index('i'))
print(my_name.isalnum())
print(my_name.isalpha())
print(my_name.isascii())
print(my_name.isidentifier())
print(my_name.isupper())
print(my_name.islower())



decimal_number = '12334'
print(decimal_number.isdecimal())

digit_numbers = '123'
print(digit_numbers.isdigit())

white_space = " "
print(white_space.isspace())

title = "One Indian Girl"
print(title.istitle())

fruit_name = "apple"
to_justify = fruit_name.ljust(30)
print(to_justify, "is good for health")

original_string = "I love apples"
print(original_string.partition(" ,"))

new_string = "hello this is prathi hello"
print(new_string.rfind("hello"))
print(new_string.rindex("hello"))

split_string = "Welcome to our website"
print(split_string.split())

swap_string = "RoCket"
print(swap_string.swapcase())

title_string = "i love dogs"
print(title_string.title())

fill_string = "30"
print(fill_string.zfill(5))

#reverse a string

reverse_string = "prathikshaa"
print(reverse_string[::-1])

#converting it to a uppercase letter
new_string = "prathi"
uppercase_string = [text.upper() for text in new_string]
print(uppercase_string)

#looping through the string
for things in "prathi":
    print(things)