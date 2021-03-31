# Name: Zachary Gearhart
# Date: 3/22/21
# Desrip: This is a loan calculator that takes input from the user in the form of the loan amount and number of payments. It then uses functions to calculate the interest rate and the monthly payment.
# Notes: I added the try/except to catch any input error that may occur. I couldn't think of anything else that could catch an input error. The mainloop function handles all of the I/O for this program.

#imports



#functions

def mainloop():

     while True:
        try:
            loan_amount = loanamount()
            
            if loan_amount >= 500:
                payment = payments()
                if payment == 'error':
                    print('Error, Input out of range, Enter the number of payments to be made.(6-48)')
                    payment = payments()
                else:
                    pass
                interest = interestrate(loan_amount, payment)
                monthly_payment = calculate(loan_amount, payment, interest)
                print('Zachary Gearhart, Software dev')
                print('Loan amount:  $',loan_amount, 'Number of payments:', payment, 'Interest rate:',round((100 * interest), 2),'%')
                print('Your monthly payment is: $', round(monthly_payment, 2))
                
                kill = input('Would you like to enter calculate another monthly payment? Type Y or N to continue')
                if kill == 'Y':
                    continue
                elif kill =='y':
                    continue
                
                if kill == 'N':
                    break
                elif kill =='n':
                    break
                
            elif loan_amount < 500:
                print("Loans under $500 are not financed, please enter a proper loan amount")
                
            else:
                print("Invaild input, try again")
        except:
            print("Invaild input, Enter a numerical value.")
            
     print("Thank you for using this program!")
     return
    
    


def loanamount():
        try:
            loan_amount = float(input("Enter a loan amount of $500 dollars or higher : "))
            return loan_amount
        
        except:
            loan_amount = 'error'
            return loan_amount
    
def payments():
        payments = float(input('Enter the number of payments to be made,(6-48): '))
        if payments >= 6 and payments <= 48:
            return payments
     
        else:
            payments = 'error'
            return payments
        
def interestrate(loan, payments):
    if loan >= 500 and loan <= 2500:
        if payments >= 6 and payments <= 12:
            interest_rate = .08
            return interest_rate
        elif payments >= 13 and payments <= 36:
            interest_rate = .1
            return interest_rate
        elif payments >= 37 and payments <= 48:
            interest_rate = .12
            return interest_rate
                
    elif loan >= 2501 and loan <= 10000:
        if payments >= 6 and payments <= 12:
            interest_rate = .07
            return interest_rate
        elif payments >= 13 and payments <= 36:
            interest_rate = .08
            return interest_rate
        elif payments >= 37 and payments <= 48:
            interest_rate = .06
            return interest_rate

    elif loan > 10001:
        if payments >= 6 and payments <= 12:
            interest_rate = .05
            return interest_rate
        elif payments >= 13 and payments <= 36:
            interest_rate = .06
            return interest_rate
        elif payments >= 37 and payments <= 48:
            interest_rate = .07
            return interest_rate
    

def calculate(loan, payments, interest):
    monthly_interest = interest / 12
    loan_payment = (monthly_interest * loan) / (1 - (1 + monthly_interest) ** -payments)
    return loan_payment


#main

def main():
    mainloop()

    
#call
main()
