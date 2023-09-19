# PART A :  House Hunting
#INPUT
#annual_salary = float(input("enter the annual salary:"))
#portion_saved = float(input("enter the percent of your saved salary:"))
#total_cost = float(input("enter the cost of your dream house:"))
#portion_down_payment = 0.25
#r = 0.04
#INITIALIZE
#current_saving = 0
#months = 0
#CALCULATE
#down_payment =  total_cost * portion_down_payment
#LOOP
#while current_saving < down_payment:
#    monthly_saving = annual_salary/12 * portion_saved
#    current_saving += current_saving * (r/12) + monthly_saving
#   months += 1
#
#print("number of months:", months)


# PART B : Saving, with a raise Background 
#INPUT
#annual_salary = float(input("enter the annual salary:"))
#portion_saved = float(input("enter the percent of your saved salary:"))
#total_cost = float(input("enter the cost of your dream house:"))
#semi_anual_raise = float(input("enter the semi annual raise:"))
#portion_down_payment = 0.25
#r = 0.04
#INITIALIZE
#current_saving = 0
#months = 0
#CALCULATE
#down_payment =  total_cost * portion_down_payment
#LOOP
#while current_saving < down_payment:
#    monthly_saving = annual_salary/12 * portion_saved
#    current_saving += current_saving * (r/12) + monthly_saving
#    months += 1

 #   if months % 6 == 0:
#        annual_salary += annual_salary * semi_anual_raise

#print("number of months:", months)


#PART C: Finding the right amount to save away

#Constants
total_cost = 1000000  
semi_annual_raise = 0.07  
annual_return = 0.04  
months = 36  

#input
starting_salary = float(input("Enter your starting annual salary: "))

#Initialize 
low = 0  
high = 10000  
steps = 0

while low <= high:
    steps += 1
    savings_rate = (low + high) / 20000  

    # Initialize 
    current_savings = 0
    monthly_salary = starting_salary / 12

    for month in range(months):
        current_savings += current_savings * (annual_return / 12) + monthly_salary * savings_rate

        if month % 6 == 0:
            monthly_salary += monthly_salary * semi_annual_raise

    # Check if savings are within $100 of the down payment
    if abs(current_savings - total_cost * 0.25) < 100:
        print("Best savings rate:", round(savings_rate, 4))
        print("Steps in bisection search:", steps)
        break
    elif current_savings < total_cost * 0.25:
        low = int(savings_rate * 10000) + 1  
    else:
        high = int(savings_rate * 10000) - 1  
else:
    print("It is not possible to pay the down payment in three years.")

