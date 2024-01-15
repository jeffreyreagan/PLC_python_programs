import os
import sys
import time

'''
Get time and date from datetime import date'

print(time.strftime("%a, %d %b %Y %H:%M:%S")

FOR LOOP THROUGH A LIST
add an item to a list with append'''

fruitss = ["apple", "banana", "cherry"]
for x in fruitss:
    if x == "banana":
      fruitss.append("grape")
      print(fruitss)

'''skip an item in a list with continue'''
for x in fruitss:
    if x == "grape":
        continue
    print(x)

'''to leave a FOR LOOP, use break: will leave loopbefore last mentioned str'''
for x in fruitss:
    if x == "banana":
        break
    print(x)





'''DICTIONARIES
FORM A DICTIONARY, GET A STRING OUT OF VARIABLE WITH VARiABLE.GET("str")
Change the value of a key inside a dictionary'''

car =	{
  "brand": "Subaru",
  "model": "STI",
  "year": 2020
}
car["year"] = 2021

'''for loop to get the value inside a variable using var.get("key"), print this, break to leave loop'''
for x in car:   
    print(car.get("brand"))
    break

'''another example'''
info = {"name" : "Jeff", "age" : 21}
#display x:
print(info)
#display the data type of x:
print(type(info)) 
for x in info:
	print(info.get("name"))
	break




'''FORMAT
Use format to use the value of a variable inside the conditions of another'''
age = 21
txt = "My name is Jeff, and I am {}"
print(txt.format(age))

''' add the str of one set to the str of another set with var.update(var_added)'''
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

'''tuple: len(var) calculates number of strings in variable'''
#  var = ("str1", "str2")  lists 
fruits = ("apple", "banana")
print(fruits)
print(len(fruits))

'''tuple use specific strings in a list Var[starting#, final#]'''
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

'''while true loop with break'''
while True:
        print("hi elly i missed you")
        time.sleep(1)
        print("I Love You")
        break

'''unpack a list or tuple into variables'''
'''Unpack a list:'''
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)





'''global

If you create a variable with the same name inside a function, 
this variable will be local, and can only be used inside the function.
The global variable with the same name will remain as it was, global and with the original value.'''

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
'''         Outside of scope x is still set until fuction is called'''
print(x)
myfunc()
print("Python is " + x)

'''If you use the global keyword, the variable belongs to the global scope:
Also, use the global keyword if you want to change a global variable inside a function.'''
x = "wont print"
def myfunc():
  global x
  x = "fantastic"
'''set new global for x'''
myfunc()

print("Python is " + x)

'''Great example of using a function and global to control variable output'''
x = "haha"
def myfunc():
  global x
  x = "fantastic"
'''                    print x before function called'''
print(x)
myfunc()
'''                    print x after global x'''
print(x)
print("Python is " + x)

while True:
  y = 2
  def y_3():
    global y
    y = 3
    print(y)
  y_3()
  print(y)
  print(type(y))
  break




