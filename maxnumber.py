# input number will be taken by input keyword
first= int(input("Enter first number: "))
second= int(input("Enter second number: "))
third= int(input("Enter third number: "))

#using the conditions
if (first > second) and (first > third):
   maximum = first
elif (second > first) and (second > third):
   maximum = second
else:
   maximum = third
 
print("The largest number is",maximum)
