import math

# possible look at using ElectronJS for a frontend and develop flask backend
# using this file as a POC

# make method that will allow the user to calc monthly payments
# required in order to pay off debt in X years

# make method that will compare two loans and determine what one should
# be payed first and down to which amount

# create method that will calculate total amount paid given principal, apy, years

"""This method will return the number of months needed to pay off a loan given
the principal, apy, and monthly payments"""
def calcNumberOfPayments(principal, apy, monthly_payment):
    # check apy to make sure it's in decimal form and convert if needed
    rate = apy
    if rate >= 1.0:
        rate = percentageToDecimal(apy)
    # calc monthly create
    monthly_rate = rate/12

    numerator = math.log10(1 - monthly_rate * principal / monthly_payment) * -1
    denominator = math.log10(1+monthly_rate)
    return numerator / denominator

def calcTotalInterestPayed(principal, monthly_payment, num_payments):
    return 0

def percentageToDecimal(percentage):
    return percentage / 100

def decimalToPercentage(decimal):
    return decimal * 100

# this method will calculate how much interest will be accrued during a period
# Range: year - daily I.E. yearly=1|daily=365
def calcInterestAccrued(principal, apy, interval):
    # check apy to make sure it's in decimal form and convert if needed
    rate = apy
    if rate >= 1.0:
        rate = percentageToDecimal(apy)
    # verify interval in no greater than 365, since 365 would signify Daily
    if interval > 365:
        # kick out an error about how daily is as far down as it goes
        print("Interest accrued can be calculated on a daily basis at most.")
        return
    # calc the interest for the given interval
    rate = rate / interval
    # calc yearly interest total
    return principal * rate

def main():
    print("Tests below: /n")

    #monthly = calcMonthlyInterestAccrued(1000, .05)
    months = calcNumberOfPayments(10000, 10, 500)
    print(months)

main()
