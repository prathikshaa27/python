#list practice questions
#website for practice questions:https://www.geeksforgeeks.org/python-exercises-practice-questions-and-solutions/

#interchange the first and last element
new_list=[1,2,3,4,5]
new_list[0]=5
new_list[4]=1
print(new_list)

#swap two elements
swap_list = ["apple","mango","orange"]
swap_list[0],swap_list[1]= swap_list[1],swap_list[0]
print(swap_list)

#max of two numbers in python
first_number = 12
second_number=20
if first_number>second_number:
    print(f"First number is the largest :{first_number}")
else:
    print(f"Second number is the largest :{second_number}")

#min of 2 numbers 
third_number = -1
fourth_number = -12
if third_number<fourth_number:
    print(f"The smallest no is: {third_number}")
else:
    print(f"The smallest number is : {fourth_number}")

#check element exists
fruit_list = ["apple","mango","grapes"]
if "kiwi" in fruit_list:
    print("found")
else:
    print("Not found")