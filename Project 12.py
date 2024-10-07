def DecimalToBinary(num):

    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2,end = "")
if __name__ == '__main__':
    dec_val = int(input("Please enter the number you'ed like to caculate to binary: "))



    DecimalToBinary(dec_val)