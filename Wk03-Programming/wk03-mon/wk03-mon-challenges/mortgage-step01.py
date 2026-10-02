
MONTHS_PER_YEAR = 12
STAMP_DUTY_RATE = 0.01     # 1% on properties under €1M

def monthly_rate(annual_rate):
    one_month_rate = annual_rate / 12
    return one_month_rate

def n_payments(years):
    num_lifetime_payments = years * MONTHS_PER_YEAR
    return num_lifetime_payments

def monthly_payment(principal, annual_rate, years):
    #r = annual_rate / 12 
    r = monthly_rate(annual_rate)
    print(f"r = {r}")
    n = n_payments(years) # number of life time payments
    #num_lifetime_payments = years * MONTHS_PER_YEAR
    print(f"n = {n}")
    factor = (1 + r) ** n   # ^ didn't work for me so used this
    print(f'factor = {factor}')
    result = principal * r * factor / (factor-1)
    #result = principal * r * (1 + r )^num_lifetime_payments / ((1+r)^num_lifetime_payments - 1): not working ^ ?
    print(f"RESULT = {result}")
    return result

payment = monthly_payment(200000, 0.04, 30)
print(f"Monthly payment: €{payment:.2f}")