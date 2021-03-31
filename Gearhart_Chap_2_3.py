# Name: Zachary Gearhart
# Date: 1/27/21
# Description: This is a program that takes the hourly pay of someone and the number of hours they work,
# In order to calculate the total pay.
# Notes: Something to remeber, the addition operator +, subtraction operator -,
# multipcation operator *, division operator /

hours = float(input('Enter the number of hours you work: '))
pay = float(input('Enter your hourly pay: '))

gross_pay = hours * pay
print('Your total pay is:', '$' + str(gross_pay)) # added a dollar sign to the gross_pay variable.
