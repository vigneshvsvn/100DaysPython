print("Welcome to the Tip Calculator!")
billAmount=float(input("Enter your Bill Amount:"))
tip=int(input("How much % tip would you like to give ? 10 or 12 or 15 ?"))
total_Splits=int(input("How many people to split the bill ?"))
splitAmount=(billAmount + (billAmount/100 * tip) )/total_Splits
print("Each Person should Pay:",round(splitAmount,2))

