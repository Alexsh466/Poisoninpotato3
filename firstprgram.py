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

#Arithmetic Operators

#Addition and Subtraction
print(5+3)
print(5-3)

#Division operators
print(5/2)
print(5//2)

#Modulus operator
print(5%2)
print(7%2)

#Exponentation
print(5 **10)
print(3 ** 2)

#Comparision/Relational Operators

#Basic Comparision
print(5 == 2)
print(5 != 3)
print(10 > 20)

#Chained Comparision

a=4
print(1 <a <5)
print(-3 <= a <=5)
print(5 < a < 7)

#String Comparision
print("cat" < "dog")
print("Cat" == "cat")

#Comparing boolean with numbers
print(1 == True)
print(0 == False)
print(1 == "1")

#Assignment Operators
 
#Compound Assingment Operators
x = 25
x += 50 
x *= 2
x -= 5
print(x)

#Multiple Assignment - helps to assign several variables in single line
a = b = c = 4
print(a,b,c)

#Tuple unpacking
a,b,c = 4,5,6
print(a,b,c)

#Swap Variables
a,x = 10, 20
a,x = x,a  #the swap occurs here
print(a,x)

#Logical Operators

#And Operator
name = "Ishan"
is_present = True
print(name =="Ishan" and is_present)

#Or Operator
name = "Ishan"
is_present = False
print(name =="Ishan" or is_present)

#Not Operator
print(not True)
print(not False)

#Short Circuit with and - right side is skipped if left is false
#print(True and 1/0)

#Short Circuit with or - right side is skipped if left is true
#print(1/0 or True)

#Combining Logical Operators with Comparision Operators
marks=45
print(marks >=40 and marks<=100) #True
print(marks < 40 or marks >100 ) #False

#Bitwise Operators

#AND -1 only where both bits are 1
print(5&3)

#bin shows the binary representation of any number
print(bin(4))

#OR -1 where either bit is 1
print(5|3)

#XOR -1 where bits are different
print(5^3) # for eg if there is same bits such as 1 and 1 then the result is 0 but if there is diff such as 0 and 1 then the result is 1

#Left shift  multiple by powers of 2
print(5 << 1) # 5 * 2 #binary digits move to left
print(5 << 2) # 5 * 4

#Right shift - divide by powers of 2
print(20 >> 1) #20 divied by 2
print(20 >> 2) #20 divied by 4

#Not sign is interchanged and the value is increased by one i.e +-(n+1)
print(~6)  #Answer is -7
print(~ -7) #Answer is 8

#Membership Operators -checks if value exists in a sequence
print("Soft" in "Softwarica") #True 
print("Cls" in "Class") #False
print("pre" in "Present") #False since python is case sensitive

#Identity = checks value equality, is checks object memory
a = [2,3,4]
b = [2,3,4]
c=a

print(a is b) #False since their value equality is same but object memory is different
print(a is c) #True
print(a ==b) #True
print(a ==c) #True

#To check address of the object
print(id(a))
print(id(b))
print(id(c))