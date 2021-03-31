# Name: Zachary Gearhart
# Date: 3/6/21
# Description: This program is a rewrite of the grade program from the previous chapters,
# It uses functions to calculate grades.
# Notes

# imports go here


# functions go here
def computegrade(score):
    if score > 1.0:
        score = 'Bad input, try again'
        return score
    elif score >= .9:
        score = 'A'
        return score
    elif score >= .8:
        score = 'B'
        return score
    elif score >= .7:
        score = 'C'
        return score
    elif score >= .6:
        score = 'D'
        return score
    elif score < .6:
        score = 'F'
        return score
    else:
        score = 'Bad input, try again'
        return score


# def main goes here
def main():
    score = float(input('Enter a your grade in decimal form, ex: 90 = .9'))
    print(computegrade(score))


# call to main goes here
main()
