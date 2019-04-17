first= int(input("Enter first number: "))
second= int(input("Enter second number: "))
third= int(input("Enter third number: "))
 
if (first > second) and (first > third):
   maximum = first
elif (second > first) and (second > thrid):
   maximum = second
else:
   maximum = thrid
 
print("The largest number is",maximum)
