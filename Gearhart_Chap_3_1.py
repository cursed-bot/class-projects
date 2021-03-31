# Name: Zachary Gearhart

# Date: 2/7/21

# Description: This is a program that takes the hourly pay of someone and the number of hours they work,
# In order to calculate the total pay. If the pay is over $40 dollars, the persons
# hourly is multipied by 1.5

# Notes: Something to remeber, the addition operator +, subtraction operator -,
# multipcation operator *, division operator /. And an indent is four spaces.

#IPO

#Input

Hours = float(input('Enter the number of hours you work. 0-100: '))

Pay = float(input('Enter your hourly pay. 0-100: '))

#Process

if Hours > 40:
    Pay = Pay * 1.5
else:
    pass # Added an else statment to close off the if statement, and it makes it easier for more conditions to be added later

Gross_pay = Hours * Pay

#Output

print('Your total pay is:', '$' + str(Gross_pay)) # added a dollar sign to the Gross_pay variable.
