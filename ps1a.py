#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 05:51:36 2021

@author: vanessamsantana
"""

#total_cost = 0
current_savings = 0
portion_down_payment = 0.25
r = 0.04 #annual return at end of each month
monthly_invest_return = 0


# annual_salary = 0
# portion_saved = 0.10


# Write a program to calculate how many months it will take you to save up enough money for a down payment.
# You want your main variables to be floats
# Type cast user input to floats

# Program asks the user the following input:
    # The starting annual salary (annual_salary)
    # The portion of salary to be saved (portion_saved)
    # The cost of your dream house (total_cost)


annual_salary = input("Enter your annual salary: ")
annual_salary = float(annual_salary)
#print(annual_salary)
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
portion_saved = float(portion_saved)
total_cost = input("Enter the cost of your dream home: ")
total_cost = float(total_cost)




downpayment_months = 0 #Initally set to 0, but was giving an answer with a result of -1 (182 VS 183)
downpayment_amount = total_cost*portion_down_payment #250,000

monthly_salary = annual_salary/12

while  (current_savings <= downpayment_amount):
    current_savings = current_savings + (monthly_salary * portion_saved)

    #monthly_invest_return = current_savings*(r/12)
    current_savings = current_savings + monthly_invest_return
    monthly_invest_return = current_savings*(r/12)

    downpayment_months = downpayment_months + 1

downpayment_amount = str (downpayment_amount)
downpayment_months = str(downpayment_months)
current_savings  = str(current_savings)

print()
print("Number of months: " + downpayment_months)
print("Down payment amount: $" + downpayment_amount)
print("Current savings: " + current_savings)




# Enter your annual salary: 120000

# Enter the percent of your salary to save, as a decimal: 0.10

# Enter the cost of your dream home: 1000000

# Number of months: 183
# Down payment amount: $250000.0
# Current savings: 251569.61633503888


# Enter your annual salary: 80000

# Enter the percent of your salary to save, as a decimal: 0.15

# Enter the cost of your dream home: 500000

# Number of months: 105
# Down payment amount: $125000.0
# Current savings: 125472.55033742028