#Enter the number 
n=int(input("enter tables"))

for i in range(1,n+1):
    for a in range(1,11):
        print(i,"x",a,"=",a*i)
        
    print("\n")
