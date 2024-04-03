import re

pattern = r'prathi'
new_text = "Hello this is prathi"
to_search = re.search(pattern,new_text)
if to_search:
    print("Pattern found:", to_search.group())
else:
    print("Pattern not found")

#metacharacters

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

emails =[
    "prathi@gmail.com",
    "john12@gmail.com,"
    "123@gamil.com"
]
for email in emails:
    to_find = re.search(email_pattern,email)
    if to_find :
        print(f"Valid: {email}")
    else:
        print(f"Not valid: {email}")

#character classes
vowels_set = r'[aeiou]'
sample_text = "Iam from Coimbatore"
to_find_match = re.findall(vowels_set,sample_text)
print(to_find_match)

new_place = "Taj Mahal"
pattern_start = r'^Taj'
pattern_end = r'Mahal$'
 
if(re.match(pattern_start, new_place)):
    print(f"Found : {pattern_start}")
else:
    print("Not found")

if(re.search(pattern_end, new_place)):
    print(f"Found: {pattern_end}")
else:
    print("Not found")

example_text = " welcome to our website"

#checking if the strung as hany m,e,w caharacters
to_find= re.findall("[mew]",example_text)
print(to_find)
if to_find:
    print("found")
else:
    print("Not found")

to_find = re.findall("[e-o]",example_text)
print(to_find)

#to chexk if the string has other character than erw
to_find=re.findall("[^erw]",example_text)
print(to_find)

#check if it has any digits
digits = "The time is 2 PM but till I didnt have lunch"
to_find = re.findall("[2]",digits)
print(to_find)

#split
fruits_list ="Apple,Mango,Grapes"
new_pattern = r','
to_split = re.split(new_pattern,fruits_list)
print(to_split)

#replace
text = "Hello this is prathi"
pattern = r'prathi'
to_change = "mike"
after_modified = re.sub(pattern,to_change,text)
print(after_modified)

#flags
text = r'Hi this is PRAT'
pattern = "prat"
to_match = re.search(pattern, text, re.IGNORECASE)
if to_match:
    print("Found:", to_match.group())
else:
    print("No match")

#multiline
pattern2 =r'^The'
text2 = "The lion is the king of jungle\n The Ganges is a river"
match = re.search(pattern2,text2,re.MULTILINE)
if match:
    print("Found:",match.group())
else:
    print("Not found")

#dotall - matches all character ncluding the new line
pattern3 = r'.*'
text3= "The lion is the king of jungle\nThe Ganges\nis a river"
match3 = re.search(pattern3,text3,re.DOTALL)
if match3:
    print(match3.group())
else:
    print('Nothing')

#ASCII - matches only lowercase characters
pattern4 = r'[a-z]+'
text4 = "The ganges"
match4 = re.search(pattern4,text4,re.ASCII)
if match4:
    print(match4.group())
else:
    print("Not found")
