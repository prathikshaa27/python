#lambda functions
add_numbers = lambda first_number, second_number:first_number+second_number
print(add_numbers(10,20))

#single expression
squared_numbers = lambda new_number:new_number**2
print(squared_numbers(17))

#no return statement
doubled_numbers = lambda random_number:random_number*2
print(doubled_numbers(8))

#multiple arguments
multipl_numbers = lambda number1,number2,number3:number1*number2*number3
print(multipl_numbers(2,2,2))

#map
list_numbers = [1,2,3,4,5]
to_square = list(map(lambda number:number**2, list_numbers))
print(to_square)

#filter
to_filter = list(filter(lambda numbers:numbers%2==0,list_numbers))
print(to_filter)

#decorators
def new_decorator(func):
    def internal_fun():
        print("Before function call")
        func()
        print("After function call")
    return internal_fun
 
@new_decorator
def greet():
    print("Hello this is prathi")

greet()

#clas decorators
class Decorator:
    def __init__(self,fun):
        self.fun=fun
    def __call__(self,*args,**kwds):
        print("before function call")
        result = self.fun(*args,**kwds)
        print("After function call")
        return result
    
@Decorator
def new_function(x):
    print(f" {x}")
new_function("prathi")

#passing arguments to decorators

def my_decorator_with_args(num1, num2):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator arguments: {num1}, {num2}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@my_decorator_with_args(12,13)
def my_function(x):
    print(f"Function usomg argument: {x}")

my_function("prathi")

#pre defined decorators
class PreDefinedDecorators:
    @staticmethod
    def static_method():
        pass
    @classmethod
    def class_method(cls):
        pass
    @property
    def property(self):
        pass

#chaining decorators

def first_decorator(func):
    def wrapper(*args,**kwargs):
        print("First Decorator")
        return func(*args, **kwargs)
    return wrapper

def second_decorator(func):
    def wrapper(*args, **kwargs):
        print("Second Decorator")
        return func(*args, **kwargs)
    return wrapper

@first_decorator
@second_decorator

def to_chain():
    print("Chained decorators")
to_chain()
    