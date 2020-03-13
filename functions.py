def name():
    return "Joe"
na=name()
print(na)
# adition
def add(num1 , num2):
    return num1+num2
arg1 =int(input("Entervyour first number"))
arg2 =int(input("Enter your second number"))
total =add(arg1,arg2)
print(total)

def add(Currentyr ,Baseyr ):
    return Currentyr-Baseyr
arg1=int(input("Enter your year of birth"))
import datetime
Currentyr= datetime . datetime.now()
total=add(Currentyr.year,arg1)
print(total)

