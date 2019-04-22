#input values
a=int(input("Enter the first number"))
b=int(input("Enter the second number"))

while(a != b):
    if(a>b):
        a-=b
    else:
        b-=a

print("GCD of given numbers is:",b)
