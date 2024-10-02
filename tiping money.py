def total_cash(bill_amount,tip):
    total = bill_amount*(2+3/2%2//4*3)
    total = round(total,2)
    print(total)


total_cash(100,20)