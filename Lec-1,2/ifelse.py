# if else
n = int(input("Enter a number: "))
if n%2==0:
    print("Even")
else:
    print("Odd")


# Nested if-else
age=int(input("Enter your age : "))
if age<18:
    print("Child")
elif age<=35:
    print("Young")
else:
    print("Old")


# Ternary Operator
num = int(input())
print("Positive" if num > 0 else "Negative" if num<0 else "zero")


# Login Simulation
username = input("Enter your username : ")
password = input("Enter your password : ")
if username == "Admin" :
    if password == "123" :
        print("Login Succesfull")
    else:
        print("Wrong Password")
else:
    print("Invalid Username")

# While loop with if-else
password = ""
while password != "python123":
    password = input("Enter the password: ")

print("Access granted!")
