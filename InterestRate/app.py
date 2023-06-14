#inputs principal, apr, years
#claculate the monthly payment and presenting it to the user

def main():
    print("")
    print("Monthly Payment Loan Calculator")
    print("")
    
    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate: "))
    years = int(input("Input the amount of years: "))

    monthly_interest_rate = apr/1200
    months = years * 12
    monthly_payment = principal * monthly_interest_rate /(1 - (1 + monthly_interest_rate)**(-months))

    print("The monthly payment for this loan is: %.2f" %monthly_payment)

main()
