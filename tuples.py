new_tuple = ("summer", "winter", "autumn", "spring","summer")
print(new_tuple)

#creating a tuple with single item
single_tuple = ("apple",)
print(type(single_tuple))
print(single_tuple)

#length
print(len(new_tuple))

#accessing tuples
print(new_tuple[2])
print(new_tuple[-1])
print(new_tuple[0:2])

#check if item exists
if "summer" in new_tuple:
    print("Found")
else:
    print("Not found")

#converting to a list and the adding the items
x = list(new_tuple)
x.append("snow")
new_tuple=tuple(x)
print(x)

#unpacking the tuples
no_of_clothes = ["denims", "shirts", "tops"]
[cloth1, cloth2,cloth3] = no_of_clothes
print(cloth1)
print(cloth2)
print(cloth3)

#Lopping
this_tuple = ("flipkart", "amazon", "myntra")
for things in this_tuple:
    print(things,len(things))

#joining tuples

first_tuple = ("braclets","earrigs","choke")
second_tuple = ("rings", "clips","clutch")
to_join_tuples = first_tuple+second_tuple
print(to_join_tuples)

#multiply tuples
to_multiply_tuple = first_tuple*2
print(to_multiply_tuple)

#tuple methods
#count
print(new_tuple.count("summer"))

#index
print(new_tuple.index("winter"))