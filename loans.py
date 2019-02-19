import math

# possible look at using ElectronJS for a frontend and develop flask backend
# using this file as a POC

# make method that will allow the user to calc monthly payments
# required in order to pay off debt in X years

# make method that will compare two loans and determine what one should
# be payed first and down to which amount

def percentageToDecimal(percentage):
    return percentage / 100

def decimalToPercentage(decimal):
    return decimal * 100

"""This method will return the number of months needed to pay off a loan given
the principal, apy, and monthly payments"""
def calcNumberOfPayments(principal, apy, monthly_payment):
    # check apy to make sure it's in decimal form and convert if needed
    rate = apy
    if rate >= 1.0:
        rate = percentageToDecimal(apy)
    # calc monthly create
    monthly_rate = rate / 12
    # calc number of months
    numerator = math.log10(1 - monthly_rate * principal / monthly_payment) * -1
    denominator = math.log10(1 + monthly_rate)
    return round(numerator / denominator, 2)

"""This method will calculate the total interest payed given principal, apy, and
monthly payments"""
def calcTotalInterestPayed(principal, apy, monthly_payment):
    num_months = calcNumberOfPayments(principal, apy, monthly_payment)
    return monthly_payment * num_months - principal

"""This method will calculate the monthly payment needed to pay off a loan
in a given number of months"""
def calcMonthlyPaymentForNumberOfMonths(principal, apy, months):
    # check apy to make sure it's in decimal form and convert if needed
    rate = apy
    if rate >= 1.0:
        rate = percentageToDecimal(apy)
    # calc monthly create
    monthly_rate = rate / 12
    # calc monthly payment
    numerator = monthly_rate * principal
    denominator = 1 - (1 + monthly_rate) ** (-1 * months)
    return round(numerator / denominator, 2)

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
    interest_payed = calcTotalInterestPayed(10000, 10, 500)
    monthly_payment = calcMonthlyPaymentForNumberOfMonths(10000, 5, 36)
    test = calcTotalInterestPayed(10000, 5, monthly_payment)
    print(months)
    print(interest_payed)
    print(monthly_payment)
    print(monthly_payment * 36)
    print(round(test, 2))

main()
