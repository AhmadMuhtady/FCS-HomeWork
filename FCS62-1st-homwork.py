# Nabiha, a software engineering consultant, receives a variable salary every month. She wants to create a Python script that helps her manage her monthly finances by calculating how much money will be allocated to different categories like savings, rent, and electricity, based on percentages of his salary.

# Your task is to write a Python script that automates these calculations. The script should:


# • Ask Nabiha to input her salary for the month.
# • Ask Nabiha to input the name of the month she is storing the salary for.
# • Ask Nabiha to input the following percentages for: a) Savings b) Rent c) Electricity

# The script should calculate and display:


# • The amount allocated to savings, rent, and electricity.
# • The total amount Nabiha spends on savings, rent, and electricity combined.
# • The remainder of Nabiha’s salary after these expenses.
# • The monthly rent and electricity multiplied by 12 to estimate Nabiha's yearly rent and electricity costs.
# • Nabiha's total salary for the month raised to the power of 2 (just for fun).
# • Assume Nabiha saves an additional random amount (e.g., $50) each month, and you need to calculate how much would be left if this amount is divided by the total amount allocated to savings. 

# Finally, the script should output all the results in a readable format.

Salary = int((input("Enter your salary for the month: ")))
Month = str(input("Enter the name of the month you are storing the salary for: "))
savings_percentage = float(input("Enter the percentage of your salary you want to allocate to savings: ")) / 100
rent_percentage = float(input("Enter the percentage of your salary you want to allocate to rent: ")) / 100
electricity_percentage = float(input("Enter the percentage of your salary you want to allocate to electricity: ")) / 100
extra_savings = int(input("Enter the amount you want to save extra: "))
