new_dict = {
    "Name":"Mike",
    "Breed" : "Dalmation",
    "Color" : "Brown and White"
}
print(new_dict)
new_dict["Age"]= 15
new_dict["Age"] = 20
print(new_dict)
print(new_dict)
new_dict.update({"Color":"Brown with White"})
print(new_dict)


#length
print(len(new_dict))

#accessing a item
print(new_dict["Name"])
print(new_dict.get("Breed"))

#printing  the keys and values separately
print(new_dict.keys())
print(new_dict.values())

#items = return dict items a tuples 
print(new_dict.items())

#checking the key exists
if "Breed" in new_dict:
    print("Present")

#removing items

original_dict = {
    "Name" : "Prathi",
    "Age" : 22,
    "Address" : 'xyz nagar'
}
print(original_dict)
print(original_dict.pop("Age")) #removes the sepcific item
print(original_dict)
print(original_dict.popitem()) #remove sthe last added item
print(original_dict)
to_clear=original_dict.clear()
print(original_dict)

del original_dict
#print(original_dict)

#Looping in dict
for things in new_dict: # to get the keys
    print(things)

for things in new_dict: #to get the values
    print(new_dict[things])

#another way to retrieve the keys and values
for things in new_dict.keys():
    print(things)

for things in new_dict.values():
    print(things)


for things in new_dict.items():
    print(things)

#copy the dictionary
print(new_dict.copy())
to_copy_dict = dict(new_dict)
print(to_copy_dict)

#nested dictionary

nested_dict ={
    "earth":{
        "color":"blue",
        "shape":"circle"
    },
    "milkiway":{
        "color":"white",
        "shape":"oval"
    },
    "sun":{
        "color":"yellow",
        "shape":"circle"

    }
    
}
print(nested_dict)
print(nested_dict["earth"]["shape"])

#dict methods
#setdefault - return a specifuc key
retrieve_key = new_dict.setdefault("Name")
print(retrieve_key)

#from keys
#returns with specific key and specific value
new_key = ("a","b","c")
some_value = 0
total = dict.fromkeys(new_key,some_value)
print(total)
print(sorted(new_dict))
print(list(new_dict))
