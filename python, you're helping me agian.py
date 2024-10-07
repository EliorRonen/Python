try:
    num1,num2 = eval(input("Please enter 2 numbers seperated by a comma:"))
    result = num1 / num2
except ZeroDivisionError:
    print("there is a zerodivistion error")
except SyntaxError:
    print("why aren't you following the rules?")
except:
    print("there are no errors")
finally:
    print("this will always apear in the code no matter what")