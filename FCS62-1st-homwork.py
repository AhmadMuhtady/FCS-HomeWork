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

action = "yes"
while action != "no":  
    Salary = int((input("Enter your salary for the month: ")))
    Month = str(input("Enter the name of the month you are storing the salary for: "))
    savings_percentage = float(input("Enter the percentage of your salary you want to allocate to savings: ")) / 100
    rent_percentage = float(input("Enter the percentage of your salary you want to allocate to rent: ")) / 100
    electricity_percentage = float(input("Enter the percentage of your salary you want to allocate to electricity: ")) / 100
    extra_savings = int(input("Enter the amount you want to save extra: "))
    action = input("Do you want to enter another Financial repot? (Enter 'no' to stop) ")


savings= Salary * savings_percentage
rent = Salary * rent_percentage
electricity = Salary * electricity_percentage
total_monthly_expenses = savings + rent + electricity
remaining_salary  = Salary - total_monthly_expenses
annual_rent = rent * 12
annual_electricity = electricity * 12
annual_savings = savings * 12
annual_salary = Salary * 12
total_annual_expenses = total_monthly_expenses * 12
annual_remaining_salary = remaining_salary * 12
bonous_salary = Salary ** 2
annual_extra_savings = extra_savings * 12
remaining_amount = annual_extra_savings / savings

financal_overview = {
    "Salary": Salary,
    "Month": Month,
    "Savings": savings,
    "Rent": rent,
    "Electricity": electricity,
    "Total_monthly_expenses": total_monthly_expenses,
}
print("\n       Financial Overview for", Month)
print("=" * 45)
print(f"{'Balance':<16}{'Monthly Amount':<16}{'Annual Amount'}")
print("=" * 45)
print(f"{'Savings':<16}${savings:<16}${annual_savings:.1f}")
print(f"{'Rent':<16}${rent:<16}${annual_rent:.1f}")
print(f"{'Electricity':<16}${electricity:<16.1f}${annual_electricity:.1f}")
print("_" * 45)
print(f"{'Total Expenses':<16}${total_monthly_expenses:<16}${total_annual_expenses:.1f}")
print(f"{'Salary':<16}${Salary:<16}${annual_salary:.1f}")
print("_" * 45)
print(f"{'Remaining':<16}${remaining_salary:<16}${annual_remaining_salary:.1f}")
print("=" * 45)
print(f"{'Bonous Salary':<16}${bonous_salary:.1f}")
print("=" *45)  
print(f"{Salary:<16.1f}${Salary}")
print(f"{'Savings':<16}%{savings_percentage*100}")
print(f"{'Extra savings':<16}${extra_savings:.1f}")
print(f"{'Remaining amount':<16} {remaining_amount:.1f} " + 'month of saving yearly')
print("=" * 45)