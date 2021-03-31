# Name: Zachary Gearhart

# Date: 2/7/21

# Description: This is a program that will prompt a user to input a float value between
# between 0.0 and 1.0 and it will give feedback depending on the value given

# Notes: Using the try/except statements proved to be very useful as it kept the code from crashing.

#IPO

#Input
try:
    Score = float(input('Type a score between 0.0 and 1.0: '))
    while Score < 0.0 or Score > 1.0:
        print('invaild input, try again')
        Score = float(input('Type a score between 0.0 and 1.0: '))
except:
    print('invaild input, try again')
    Score = float(input('Type a score between 0.0 and 1.0: '))
    
#Process

if Score >= .9:
    Score = 'A'
    
elif Score >= .8:
    Score = 'B'
    
elif Score >= .7:
    Score = 'C'
elif Score >= .6:
    Score = 'D'
    
elif Score < .6:
    Score = 'F'

#Output

print(Score)
