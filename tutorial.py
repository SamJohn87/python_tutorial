""" a = "Hello World!"
print(a) """

#input method
""" name = input("What is your name?")
print('Welcome to Python tutorial ' + name) """

#variables
""" a=7
_someVariable="Variable value"
Another_variable ="Other value" """

#Type Casting
""" a = 7
print(type(a))

b = 38.90
print(type(b)) """

#operators
""" x = 7
y = 8

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y) """

#lists
""" list1 = ["BMW", "Tesla", "Audi", "Mercedes"]
print(list1)
print(len(list1))
print(list1[0])"""

#tuples
""" tup1 = ("BMW", "Audi", "Mercedes")
print(tup1)
print(len(tup1))
print(tup1[0]) """

#sets
""" set1 = {"BMW", "Audi", "Mercedes"}
print(set1)
print(len(set1))
print(set1) """

#dictionaries
""" dict1 = {
    "car1" : "BWM",
    "car2" : "Audi",
    "car3" : "Mercedes"
}
print(dict1)
print(len(dict1))
print(dict1["car1"]) """

#conditions
""" a = 7
b = 1
if b > a:
    print("b is greater than a")
elif b==a:
    print("b is equal to a")
else:
    print("b is not greater than a") """

#loops
#while loop
""" i = 1
while i < 5:
    print(i)
    i+=1 """

#for loop
""" list1 = ["BMW", "Tesla", "Audi", "Mercedes"]
for i in list1:
    print(i) """

#function
""" def hello(fname, lname):

    print("Hello " + fname + " " + lname)

hello("Samantha", "Johnson") """

#Buit-in Math
""" x = min(3,9,7,19)
b = max(7,8,2,71,8)

print(x)
print(b) """
""" 
x = abs(-99.75) #only post positive values
print(x) """

""" x = pow(4,3)
print(x) """

#lambda function
""" a = lambda x: x*10
print(a(3)) """

#iterator
# __iter__(), __next__()
""" tup1 = ("BMW", "Audi", "Mercedes")
mytup = iter(tup1)
print(next(mytup))
print(next(mytup)) """

#module
import math
""" x = math.sqrt(16)
print(x) """

x = math.ceil(5.4)
y = math.floor(5.4)
print(x)
print(y)