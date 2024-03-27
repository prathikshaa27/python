def new_function():
    print("Hello this is prathi")
new_function()

#arguments
def my_function(name):
    print(name+" "+"Hi")
my_function("prathi")

def my_details(name,age,gender):
    print(name,age,gender)
    print(f"My name is {name} my age is {age} and my gender is {gender}")
my_details("prathi",22,"Female")

def no_of_kids(*kids):
    print("The last child is", kids[2])
no_of_kids("Senthil","prathi","Mike")

#args with key values

def my_family(child1,child2,child3):
    print("The first child is",child1)
my_family(child1="senthil", child2="prathi", child3="mike")

#default parameter

def solar_system(planet="earth"):
    print("The planet is", planet)
solar_system("mercury")
solar_system("venus")
solar_system()

def sum_numbers(number1,number2):
    sum_of_two_numbers= number1+number2
    return sum_of_two_numbers
result = sum_numbers(10,10)
print(result)

def number_calculation(number):
    return number/10
print(number_calculation(5))
print(number_calculation(10))
print(number_calculation(20))
print(number_calculation(8))
print(number_calculation(15))

#pass
def pass_function(num):
    pass

#positional arguments

def simple_number(number,/):
    print(number)
simple_number(3)

#keyword arguments
def random_number(*,newnumber):
    return newnumber
print(random_number(newnumber=10))

#combining position only and keyword only

def combine_function(value1,value2,/,*,value3,value4):
    print(value1*value2+value3/value4)
combine_function(2,4,value3=10,value4=5)

#recursion
def fibonocii_series(n):
    if n<=1:
        return n
    else:
        return fibonocii_series(n-1)+fibonocii_series(n-2)
for i in range(10):
    print(fibonocii_series(i))

def doc_string():
    """ hello
         haii
    """
    pass
print(doc_string .__doc__)

#function annotations

def fun_annotations(name:str,age:int)->str:
    return(f"My Name is {name} and my age is {age}")
details = fun_annotations("prathi",22)
print(fun_annotations.__annotations__)

#practice questions
def calculate_average(maths,biology,physics):
    return(maths+biology+physics)/3
print(calculate_average(45,35,35))


def reversed_string(new_string):
    return new_string[::-1]
print(reversed_string("prathi"))

#removing duplicates
def remove_duplicates(list):
    new_list = []
    for things in list:
        if things not in new_list:
            new_list.append(things)
    return new_list

print(remove_duplicates([20,21,100,21,18,19,100]))  
