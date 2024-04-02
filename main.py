import modules
import inheritance
import os
import math
import random
import datetime
import json
import sys
import builtins
from functions import new_function as nf

modules.new_student()
modules.old_student()
inheritance.dog1.sound()
nf()

print(os.getcwd())   #get the current working directory
print(os.listdir())  #files in the current directory

print(math.sqrt(25))
print(math.pi)

print(random.randint(100,200))
print(random.choice(["Chetan bhagat", "Durjoy datta", "preethi shenoy"]))

current_date= datetime.datetime.now()
print(current_date)

#convert to a json string
person_details ={"Name":"prathi", "Age": 22 ,"Native": "Coimbatore"}
to_convert = json.dumps(person_details)
print(to_convert)

print(sys.path)
print(sys.platform)  #list of directories in sys.path

#dir
print(dir(math))
print(dir(sys))
print(dir(inheritance))
print(dir(builtins))
