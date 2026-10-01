# 1 for single line
"""  
for multi line comment shift alt A

""" 
#python is dynamically typed language
name = "sunflower"
age = 99
location = "dubai"
#concate
print("my name is " +name + " and age is " +str( age) + " and my location is " +location)
#f string
print (f"my name is {name} and age is {age} also I live in {location}")
#format old version
print("my name is %s and age is %d and location is %s" %( name,age,location))
#format new version
print("my name is {0} and age is {1} and location is {2}".format( name,age,location))
#task 2
num1 = input(" Enter the num1")
num2 = input( " Enter the num2  ")
sum1 = num1 + num2
print("The sum is" +sum1 + "and the type is" + (type (sum1)))

num3 = int(input("Enter the num1"))
num4 = int(input("Enter the num2"))
sum2 = num3 + num4
print("The sum is" +(sum2) + "and the type is" + (type(sum2)))
