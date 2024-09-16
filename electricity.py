units = int(input("Please enter Number of units you Consumed:"))

if(units < 50):
    amount = units*2
    surcharge = 25
elif(units < 50):
    amount = 130 + 130((units - 50*4))
    surcharge = 35
elif(units <= 200):
    amount = 130 + 162 ((units - 100) *3)
    surcharge = 45
else:
    amount = 130 + 162 + 526 + ((units - 200) * 8)
    surcharge = 75
total = amount + surcharge
print("\nElectrictiy Bill = %.2f" %total)