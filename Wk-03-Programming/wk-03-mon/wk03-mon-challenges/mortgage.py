#my maths seem a little off, doesn't exactly match your results
# P * r * (1+r)^n / ((1+r)^n - 1)...not sure whats happening here with the ˆ
# I also returned the total interest paid, not sure if maths is right there either
MONTHS_PER_YEAR = 12
STAMP_DUTY_RATE = 0.01     # 1% on properties under €1M

def print_dashes(num_dashes, symbol,):
    print(symbol * num_dashes)

def print_banner(title, num_dashes, symbol):
    print_dashes(symbol, num_dashes)
    print(f'{title:^50}')
    print_dashes(symbol, num_dashes)

def monthly_rate(annual_rate):# rate for one moth
    return annual_rate / MONTHS_PER_YEAR

def n_payments(years):# total number of payments over the lifetime of the loan
    return years * MONTHS_PER_YEAR 

def stamp_duty(price):
    return price * STAMP_DUTY_RATE

def total_cost(n, monthly_result): # n is total number of payments, monthly _result is whats paid each month
    return n * monthly_result
    
def monthly_payment(principal, annual_rate, years, deposit): #I also calculkate the total interest paid over the life time of the loan
    total_price = principal + deposit# used to calculate stamp duty on full price not just principal
    n = n_payments(years) # number of life time payments
    ar = annual_rate #for returning the total interest paid
    mr = monthly_rate(annual_rate)
    monthly_factor = (1 + mr) ** n   # ^ didn't work for me so used this
    annual_factor = (1 + ar) ** n 
    ti_result = principal * ar * annual_factor / (annual_factor-1)#for returning the total interest paid
    monthly_result = principal * mr * monthly_factor / (monthly_factor-1)
    total_payments = n * monthly_result # calculate this here? is it beter than writing another function
    total_stamp_duty = stamp_duty(total_price)
   
    return monthly_result, total_payments, total_stamp_duty, ti_result
    
def print_mortgage_summary():
    print_banner('MORTGAGE SUMMARY', 50, "=")
    print(f'Property price: €350,000')
    print(f'Deposit: €35,000')
    print(f'Loan amount: €315,000')
    print(f'Annual rate: 4.00%')
    print(f'Term: 30 years')
    print_dashes(50, "-")
    print(f'Monthly payments: €{m_payment:.2f}')
    print(f"Total interest payment: €{ti_payment:.2f}")
    print(f'Total repaid: €{tc_payment:.2f}')
    print(f"Stamp duty = €{total_stamp_duty:.2f}")

m_payment, tc_payment, total_stamp_duty, ti_payment = monthly_payment(315000, 0.04, 30, 35000)

print_mortgage_summary()