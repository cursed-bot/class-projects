# Name: Zachary Gearhart
# Date: 2/12/21
# Description: This is a program that will calculate monthly loan payments based on
# the inputs given.
# Notes: While this program was easy to make, I could not find an effective addition to make,
# so I broke up the outputs from the input prompts

#IPO

#Input

print('This program will calculate the monthly payment of loan when given the values of')
print('the loan')

loan_amount = float(input('Enter the loan amount in decimal form, ex: 1000.0: '))

raw_interest_rate = float(input('Enter the interest rate in decimal form, ex: 5%=.05: '))
monthly_interest_rate = raw_interest_rate / 12

num_payments = float(input('Enter the total number of payments in decimal form, ex: 10.0: '))

#Process

loan_payment = (monthly_interest_rate * loan_amount) / (1 - (1 + monthly_interest_rate) ** -num_payments)


#Output

print('')

print('Name: Zachary Gearhart, Software dev')

print('The loan amount is, $', loan_amount)

print('The interest rate is',raw_interest_rate, '%')

print('The total number of payments to make is', num_payments)

print('The total monthly payment will be, $', round(loan_payment, 2), 'per month.')
