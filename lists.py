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