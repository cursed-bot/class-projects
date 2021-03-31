# Name: Zachary Gearhart
# Date: 3/5/21
# Description: This is a reworking of the pay computation program from the previous lessons
# that uses functions
# Notes:

# imports go here


# functions go here

def computepay(hours, rate):
    
     if hours <= 40:
        weeklypay = hours * rate
        return weeklypay
    
     else: 
        otrate = rate * 1.5
        othours = hours - 40
        otpay = othours * otrate
        hours = 40
        weeklypay = hours * rate
        timeandhalfpay = weeklypay + otpay
        
        return timeandhalfpay

# def main goes here

def main():
    
    hours = float(input('Please input how many hours you work in a week: '))
    payrate = float(input('Next, please input your hourly pay rate: '))
    
    print('Your pay is',computepay(hours, payrate), 'this week.')
    


# call to main goes here

main()
 
