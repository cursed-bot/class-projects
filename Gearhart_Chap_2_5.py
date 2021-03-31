# Name: Zachary Gearhart
# Date: 1/27/21
# Descpription: This is a program that asks the user for the temperature in celcius, and then converts it to fahrenheit.
# Notes: Something that I had issues with was following the order of operations
# to calculate the temperature, but I found it was easier to do the steps in order.

ctemp = float(input('Enter the temperature in celsius: '))

st1 = ctemp * 1.8

st2 = float(st1) +32

print('It is:', st2, 'degrees fahrenheit.') # added some text to the output to make it cleaner
