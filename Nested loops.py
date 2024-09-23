
string = input("Please input your email: ")

char = input("Please input the letter you'd like to count in the email: ")

i = 0

count = 0

while i < len(string):

    if string[i] == char:
      count += 1
    i += 1
print("The letter" ,char, "appears" ,count, "times in the email.")