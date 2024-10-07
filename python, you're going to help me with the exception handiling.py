try:
    n = int(input("Please input the number you'ed like:"))
    print("entered number is",n)
except ValueError as ex:
    print(ex)