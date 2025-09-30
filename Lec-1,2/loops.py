# for loop
for i in range(1,6):
    print(i, end=" ")
print() # for new line
for i in range(1,10,2):
    print(i, end=",")
print()
for i in range(1,5,3):
    print(i*2,end=" ")
print()
for i in range(10):
    print("*"*(i+1))
print()
for i in range(10,0,-1):
    print(i, end=" ")  
print()
# while loop
i =1
while(i<=10):
    print(i)
    i=i+1
print()
# continue
for i in range(1,11):
    if(i==5):
        continue
    print(i)
