# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
months = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


def get_additional_payment(count=0, start_month=0, end_month=0, payment=0.0, extra_payment=0.0):
    return payment + extra_payment if start_month <= count <= end_month else payment


while principal > 0:
    new_payment = get_additional_payment(count=months, start_month=extra_payment_start_month,
                                         end_month=extra_payment_end_month, extra_payment=extra_payment, payment=payment)
    if principal > new_payment:
        principal = principal * (1 + rate / 12) - new_payment
        total_paid += new_payment
    else:
        total_paid += principal
        principal = 0.0
        
    months += 1
    print('{} {} {}'.format(months, round(total_paid, 2), round(principal, 2)))

print('Total paid', round(total_paid, 1))
print('Months', months)
