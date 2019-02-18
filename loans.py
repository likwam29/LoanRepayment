# possible look at using ElectronJS for a frontend and develop flask backend
# using this file as a POC

# make method that will allow the user to calc monthly payments
# required in order to pay off debt in X years

# make method that will compare two loans and determine what one should
# be payed first and down to which amount

#

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
    print("Daily interest: /n")

    #monthly = calcMonthlyInterestAccrued(1000, .05)
    yearly = calcInterestAccrued(1000, 5, 2131)
    print(yearly)

main()
