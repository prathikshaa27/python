def count_numbers(n):
    count = 1
    while count<=n:
        yield count
        count=count+1

generator1 = count_numbers(10)

for numbers in generator1:
    print(numbers)


