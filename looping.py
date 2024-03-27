for i in range(1,11):
    print(i)
for i in range(0,10,3):
    print(i)

#break 
no_of_items = ["pencils", "pens","erasers"]
for things in no_of_items:
    print(things)
    if(things=="pens"):
        break

#continue
no_of_veggies = ["carrot", "beetroot","peas"]
for things in no_of_veggies:
    if(things=="beetroot"):
        continue
    print(things)

#for with else loop
for things in range(5):
    print(things)
else:
    print("example using for with else")

#nested loops
new_color =["red", "green","pink"]
new_items=["berry", "glass","salwar"]
for things in new_color:
    for things1 in new_items:
        print(things,things1)

#pass
for things in range(2,6):
    pass

#printing even numbers
for things in range(2,12,2):
    print(things)

for _ in range(5):
    print("prathi")


list_reverse = [1,2,3,4,5]
for num in reversed(list_reverse):
    print(num)

#while loop :

new_number = 1
while(new_number<=10):
    print(new_number)
    new_number=new_number+1

sample_number = 1
while sample_number <= 5:
    print(sample_number)
    if sample_number == 3:
        break
    sample_number += 1

some_number =1
while some_number<=5:
    some_number=some_number+1
    if some_number==3:
        continue
    print(sample_number)

random_number = 12
while random_number<20:
    print(random_number)
    random_number=random_number+1
else:
    print("Exampel using else in while")