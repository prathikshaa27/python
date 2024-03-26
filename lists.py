new_list =["apple","mango","grapes","pappaya","peach"]
print(new_list)

#length 
print(len(new_list))

#accessing items
print(new_list[2])

#accessing range of items
print(new_list[2:4])

#check if items exits
if "grapes" in new_list:
    print("Present")
else:
    print("Not present")

#changing the items
new_list[2]="Guava"
print(new_list)
new_list[2:3]="Bannana","Orange"
print(new_list)

#inserting a new item without replacing

new_list[2]="Cherry"
print(new_list)
print(len(new_list))

#add list items
original_list =["selvaraj", "vijayalakshmi","senthil","mike"]
original_list.append("prathi")
print(original_list)

#insert at a specific place
original_list.insert(2,"tucker")
print(original_list)

new_list.extend(original_list)
print(new_list)

#deleting the items from the list
list_delete = ["veggies","fruits","junk","veggies"]
list_delete.remove("veggies") #removes the first occurence
print(list_delete)

list_delete.pop(1) #removes based on the index
print(list_delete)

del list_delete[0]
print(list_delete)

list_delete.clear()
print(list_delete)

del list_delete

#Looping lists

list_loop=["Pencils","Pens","Erasers"]
for things in list_loop:
    print(things)

i = 0
while i<len(list_loop):
    print(list_loop[i])
    i=i+1

#sorting the list

list_sort= ["bags", "pouches","clutches","sling bags","hats"]
list_sort.sort()
print(list_sort)

#descending
list_sort.sort(reverse=True)
print(list_sort)

this_list = ["Kiwi", "bannna","Orange","grapes"]
this_list.sort(key=str.lower)
print(this_list)

#reversing a list
this_list.reverse()
print(this_list)

#copying a list 
list_copy = ["Carrot","Brocolli","Beetroot"]
list_copy.copy()
print(list_copy)

#copying using the list method
to_copy = list(list_copy)
print(to_copy)

#joining two lists

first_list = ["apple","mango","orange"]
second_list=["guava","pappaya","bannana"]
list_join=first_list+second_list
print(list_join)

#list methods
#count 
list_methods = [12,22,33,44,55,12]
print(list_methods.count(12))

#index
to_find_index = list_methods.index(55)
print(to_find_index)

#list as stacks

stack_list = ["sun", "moon", "stars"]
print(stack_list)
stack_list.append("solar system")
print(stack_list)
print(stack_list.pop())
print(stack_list)
print(stack_list.pop())
print(stack_list)

#queue

from collections import deque
queue = deque(["calender","Toys", "lights"])
print(queue)
queue.append("laptop")
print(queue)
print(queue.popleft())

#list comprehension
fruit_list = ["apple", "mango","guava","grapes","orange"]
final_list = [things for things in fruit_list if "g" in things]
print(final_list)

#filtering only even numbers
total_numbers= [1,2,3,4,5,6,7,8,9,10]
even_numbers = [even for even in total_numbers if even%2==0]
print(even_numbers)

#nested list comprehension

nested_list = [[i*j for j in range(1,4)]for i in range(1,4)]
print(nested_list)
