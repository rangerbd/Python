print("Welcome to the tip calculator!\n")
bill = float(input("what was the total bill?\n"))
tips = int(input("how much tip would you like to give? 10,12 or 15\n"))
person = int(input("how many person will split the bill?\n"))
t = tips/100
total_bill = ((tips*bill)/100)+bill
pay_per_person = total_bill/person
print(round(pay_per_person,2))
