# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
# payment = 2600
total_paid = 0.0
num_of_months = 1
# fst_yr_pmt = 3684.11

while principal > 0:
    # print(num_of_months)
    # print(principal)
   
    if num_of_months <= 12 or (num_of_months >61 and num_of_months < 108):
        principal = principal * (1+rate/12) - (payment + 1000)
        total_paid = total_paid + payment + 1000
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment 

    num_of_months = num_of_months +1  
    print(num_of_months,principal,total_paid)
    
print('Total paid', total_paid)
# print(f'no of months paid is   {num_of_months}')
print(num_of_months)
