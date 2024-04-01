bus_list = ["Essar","JB connect","VigneshTAT"]
new_iterator = iter(bus_list)
print(next(new_iterator))
print(next(new_iterator))
print(next(new_iterator))

my_name = "prathi"
some_iterator = iter(my_name)
print(next(some_iterator))
print(next(some_iterator))
print(next(some_iterator))
print(next(some_iterator))
print(next(some_iterator))
print(next(some_iterator))


class Calculate:
    def __init__(self,number):
        self.number =number
        self.index=0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >=len(self.number):
            raise StopIteration
        number=self.number[self.index]
        self.index=self.index+1
        return number
    
new_list =[8,30,25,17,1,24]
iterator1 = Calculate(new_list)

for number in iterator1:
    print(number)

