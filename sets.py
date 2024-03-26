new_set = {"mercury", "venus", "earth"}
print(new_set)

#length
print(len(new_set))

#looping
for thing in new_set:
    print(thing)
    print("earth" in new_set)

#adding items
new_set.add("mars")
print(new_set)

#add items from another set to the current set
second_set = {"jupiter", "uranus","neptune","pluto"}
new_set.update(second_set)
print(new_set)

#removing the items
new_set.remove("neptune") # if the item does not exist it will throw an error
print(new_set)
new_set.discard("uranus") # if the items does not exits it will not throw an error
print(new_set)
second_set.pop() # it will remove tge item by random
print(second_set)

#clear
original_set = {"pogo", "nick", "hungama","disney"}
print(original_set)
original_set.clear()
print(original_set)

del original_set
#print(original_set)

#join sets
set_number1 = {"apple", "mango","orange"}
set_number2 = {"grapes", "pappaya","guava"}
print(set_number1.union(set_number2))

#intersection - it returns a value which is present in both the sets it will return a common value present in both the sets
set_intersection1 = {"veggies","fruits","junk"}
set_intersection2 = {"pasteries", "ice creams","veggies"}
print(set_intersection1.intersection(set_intersection2))

#differnce
set_difference1 = {"mysql","mongodb","nosql"}
set_difference2 = {"python","react","mysql"}
print(set_difference1.difference(set_difference2))

#symmetric difference
set_symmetric1 = {"google","microsoft","amazon"}
set_symmetric2 = {"google", "firefox"}
print(set_symmetric1.symmetric_difference(set_symmetric2))

#set methods
print(new_set.copy())

#disjoint - if no same values present in both the set it will return true
find_disjointset = new_set.isdisjoint(second_set)
print(find_disjointset)

#issubset - if the same value is present in both the set it will return true
set_subset1 = {"a","b","c","d","e"}
set_subset2={"c","f","g","a","b","e","d"}
print(set_subset1.issubset(set_subset2))

#issuperset - return true if all the values in set 2 are present in set 1
set_supset1 = {"dogs","cats","birds","horses","donkeys"}
set_supset2 = {"cats","dogs","birds",}
print(set_supset1.issuperset(set_supset2))