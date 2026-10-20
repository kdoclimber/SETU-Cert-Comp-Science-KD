
MONTHS_PER_YEAR = 12
STAMP_DUTY_RATE = 0.01     # 1% on properties under €1M

def print_dashes(num_dashes, symbol,):
    print(symbol * num_dashes)

def print_banner(title, num_dashes, symbol):#takes a string
    print_dashes(symbol, num_dashes)
    print(f'{title:^50}')
    print_dashes(symbol, num_dashes)

def monthly_rate(annual_rate):
    one_month_rate = annual_rate / 12
    return one_month_rate

def n_payments(years):
    num_lifetime_payments = years * MONTHS_PER_YEAR
    return num_lifetime_payments

def stamp_duty(price):
    return price * STAMP_DUTY_RATE

def total_interest(principal, annual_rate, years):
    ar = annual_rate
    print(f"TI ar = {ar}")
    n = n_payments(years) # number of life time payments
    print(f"TI n = {n}")
    factor = (1 + ar) ** n 
    print(f'TI factor = {factor}')
    ti_result = principal * ar * factor / (factor-1)
    print(f" total interest = {ti_result}")
    return ti_result

def total_cost(n, monthly_result):
    return n * monthly_result
    
def monthly_payment(principal, annual_rate, years):
    #r = annual_rate / 12 
    r = monthly_rate(annual_rate)
    print(f"r = {r}")
    n = n_payments(years) # number of life time payments
    #num_lifetime_payments = years * MONTHS_PER_YEAR
    print(f"n = {n}")
    factor = (1 + r) ** n   # ^ didn't work for me so used this
    print(f'factor = {factor}')
    monthly_result = principal * r * factor / (factor-1)
    total_payments = n * monthly_result # calculate this here? is it beter than writing another function
   
    total_stamp_duty = stamp_duty(principal) #total_payments = total_cost(n, monthly_result)
    #result = principal * r * (1 + r )^num_lifetime_payments / ((1+r)^num_lifetime_payments - 1): not working ^ ?
    print(f"RESULT monthly_result = {monthly_result}")
    print(f"RESULT total_payments = {total_payments}")
   
    return monthly_result, total_payments, total_stamp_duty
    
def print_everything():
    print_banner('MORTGAGE SUMMARY', 50, "=")
    print(f'Property price: €350,000')
    print(f'Deposit: €35,000')
    print(f'Loan amount: €315,000')
    print(f'Annual rate: 4.00%')
    print(f'Term: 30 years')
    print_dashes(50, "-")
    print(f'Monthly payments: €{payment}')
    print(f'Total repaid: €{tc_payment}')
    print(f"Stamp Duty = {total_stamp_duty}")

    

payment, tc_payment, total_stamp_duty = monthly_payment(315000, 0.04, 30)
ti_payment = total_interest(315000, 0.04, 30)

print(f"Monthly payment: €{payment:.2f}")
print(f"Total Interest payment: €{ti_payment:.2f}")
print(f"Total Cost payment: €{tc_payment:.2f}")
print(f"Total Stamp Duty: €{total_stamp_duty:.2f}")


print_everything()