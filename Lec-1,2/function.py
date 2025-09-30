# function
# add function
def add_3(n):
    return n+3
x=8
y=add_3(x)
print(x,y)

# greetings function , printing string using function
def greetings(name):
    print("Hello",name)
name="Alexa"
greetings(name)

# greetings function through input , printing string using function
def greetings1(name):
    print("Hello",name)
name = input()
greetings1(name)

# printing string's index
country = "Bangladesh"
for c in country:
    print(c)

# multiplication table
def print_multiplication_table(n):
    for i in range (1,11):
        print(n, "X" , i ,"=", n*i)

n=int(input())
print_multiplication_table(n)