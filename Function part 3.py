def add(P,D):
    return P+D
def sub(P,D):
    return P+D
def multi(P,D):
    return P*D
def divistion(P,D):
    return P/D

print("select the operation")
print("a.add")
print("b.subtraction")
print("c.multiplication")
print("d.divistion")

choice = (input("please enter you choise a,b,c or d"))

num1 = int(input("Please enter the number you'ed like:"))
num2 = int(input("Please enter the second number you'ed like:"))

if choice == a:
    print("the result is:",add(num1,num2))
if choice == b:
    print("the result is:",sub(num1,num2))
if choice == c:
    print("the result is:",multi(num1,num2))
if choice == d:
    print("the result is:",divistion(num1,num2))