# pset2 - 1
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate / 12.0

def rem_bal( prev_bal, num_months ):
    bal = prev_bal * (1+monthlyInterestRate)
    monthlyPayment = monthlyPaymentRate * bal
    unpaid_balance = bal - monthlyPayment
    print( 12 - num_months+1 , round(unpaid_balance,2) )
    if num_months == 1:
        return unpaid_balance
    else:
        return rem_bal( unpaid_balance , num_months - 1 )

print( "Remaining balance:", round( rem_bal( balance, 12 ), 2 ) )