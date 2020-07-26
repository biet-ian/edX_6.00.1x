# pset2 - 3

balance = 999999 
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0
def rem_bal_with_fix_pay( min_fixed_payment, prev_bal, num_months ):
    monthlyPayment = min_fixed_payment
    unpaid_balance = prev_bal - monthlyPayment
    unpaid_balance = unpaid_balance * (1+monthlyInterestRate)
    # print( 12 - num_months+1 , round(unpaid_balance,2) )
    if num_months == 1:
        return unpaid_balance
    else:
        return rem_bal_with_fix_pay( monthlyPayment, unpaid_balance , num_months - 1 )

def min_monthly_pay( ):
    lower_bound = balance / 12.0
    upper_bound = ( balance * ( 1 + monthlyInterestRate)**12 ) / 12.0
    mid_pay = (lower_bound + upper_bound) / 2
    unpaid_balance = rem_bal_with_fix_pay( mid_pay, balance, 12 )
    while abs(unpaid_balance) > 0.1: 
        if unpaid_balance < 0:
            upper_bound = mid_pay
        elif unpaid_balance > 0:
            lower_bound = mid_pay
        mid_pay = (lower_bound + upper_bound) / 2
        unpaid_balance = rem_bal_with_fix_pay( mid_pay, balance, 12 )
    return mid_pay

print( "Lowest Payment:", round( min_monthly_pay(), 2) )