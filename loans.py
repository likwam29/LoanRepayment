# make method that will allow the user to calc monthly payments
# required in order to pay off debt in X years

# make method that will compare two loans and determine what one should
# be payed first and down to which amount

#

def percentageToDecimal(percentage):
    return percentage/100

def decimalToPercentage(decimal):
    return decimal * 100

def calcDailyInterestRate(apy):
    return apy/365

def calcDailyInterestAccrued(principal, apy):
    # take APY rate and get daily interest rate from it
    daily_rate = calcDailyInterestRate(apy)
    # multiply daily rate by principal
    return principal * (1 + daily_rate)

def calcMonthlyInterestRate(apy):
    return apy/12

def calcMonthlyInterestAccrued(principal, apy):
    # take APY rate and get monthly interest rate from it
    monthly_rate = calcMonthlyInterestRate(apy)
    # multiply monthly rate by principal
    return principal * (1 + monthly_rate)



def main():
    print("Daily interest: /n")

    monthly = calcMonthlyInterestAccrued(1000, .05)
    yearly = monthly + ((monthly - 1000) * 12)
    print(yearly)

main()
