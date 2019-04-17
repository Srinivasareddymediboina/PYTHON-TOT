#Enter the number 
n=int(input("enter tables"))

#single table
for i in range(1,n+1):
    #tables up to given range
    for a in range(1,11):
        print(i,"x",a,"=",a*i)
        
    print("\n")
