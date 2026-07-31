print("Hello World")

#Add two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
sum = x+y
print("The sum is:", sum)

#Add number and string
print("Number"+ str(1))

#print Name 3 times
name="Arya"
print(name)
print(name)
print(name)

#Add 3 numbers
x =int(input("Enter first number: "))
y =int(input("Enter second number: "))
z =int(input("Enter second number: "))
sum = x+y+z
print("The sum is:", sum)

#Concat 3 strings
print("Hello"+" "+"World")

#Take input from user
print(int(input("Enter a number:")))

#Print 0-10
for i in range (0, 11):
    print(i)

#Print multiple of 2
for i in range (0, 11):
    print(2*i)

#while loop
i=1
while i<11:
  print(f"2x{i}={2*i}")
  i+=1

#Print range
print("range(10)        -->", list(range(10)))
print("range(10,20)     -->", list(range(10,20)))
print("range(0,20,2)    -->", list(range(2,20,2)))
print("range(-10,-20,2) -->", list(range(-10,-20,2)))
print("range(-10,-20,-2)-->", list(range(-10,-20,-2)))

#Table of n
n=int(input("Enter n"))
i=1
while i<11:
  print(f"{n}x{i}={n*i}")
  i+=1


#add n numbers
n=int(input("Enter n"))
print(n*(n+1)/2)
