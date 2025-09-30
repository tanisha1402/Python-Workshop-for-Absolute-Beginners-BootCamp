# Taking input from the user
var = int(input("enter age : "))
var1= float(input("enter height : "))
var2 = eval(input("enter year : "))
print("Age : ",var)
print("Height : ",var1)
print("Year : ",var2)
print(type(var2))
print("Alexa","Demi","Moor") # separated by comma and prints a space automatically
print("Alexa"+"Demi"+"Moor") # concatenation
print("Alexa","Demi","Moor",sep="*") # custom separator
print("Hello",end="*") # custom end
print("World")
# multiple inputs
x,y,z = input("enter 3 values : ").split() # by default space is the separator
print("x : ",x)
print("y : ",y)
print("z : ",z)

x,y,z = input("enter 3 values : ").split(",") # custom separator
print("x : ",x)
print("y : ",y)
print("z : ",z)


