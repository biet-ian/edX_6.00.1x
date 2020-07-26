# pset2 - 2
balance = 3926 
annualInterestRate = 0.2

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
    min_pay = 10
    unpaid_balance = rem_bal_with_fix_pay( min_pay, balance, 12 )
    while unpaid_balance > 0:
        print(unpaid_balance)
        min_pay += 10
        unpaid_balance = rem_bal_with_fix_pay( min_pay, balance, 12 )
    return min_pay