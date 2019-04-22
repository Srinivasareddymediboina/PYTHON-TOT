unit1 = input ("Which unit would you like to convert from: ")
unit2 = input ("Which unit would you like to convert to: ")
num1 = float(input ("Enter your value: " ))

if unit1 == "cm" and unit2 == "m":
    print("%s m" %(num1/100))
elif unit1 == "mm" and unit2 == "cm":
    print("%s cm" %(num1/10))
elif unit1 == "m" and unit2 == "cm":
    print("%s cm" %(num1*100))
elif unit1 == "cm" and unit2 == "mm":
    print("%s mm" %(num1*10))
elif unit1 == "mm" and unit2 == "m":
    print("%s m" %(num1/1000))
elif unit1 == "m" and unit2 == "mm":
    print("%s mm" %(num1*1000))
elif unit1 == "km" and unit2 == "m":
    print("%s m" %(num1*1000))
elif unit1 == "m" and unit2 == "km":
    print("%s km" %(num1/1000))
elif unit1 == "mm" and unit2 == "km":
    print("%s km" %(num1/1000000))
