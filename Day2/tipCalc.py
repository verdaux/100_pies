print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage = int(input("How much tip would you like to give? 10,12,or 15? "))
people = int(input("How many people to split the bill? "))

tip_amount = (tip_percentage/100)*total_bill
added_tip_amount = tip_amount+total_bill
final_amount_pp = round(added_tip_amount/people,2)

print(f"Each person should pay {final_amount_pp}")