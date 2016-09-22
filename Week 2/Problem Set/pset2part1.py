# -*- coding: utf-8 -*-
"""
Created on 21/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

balance = float(input('Balance = '))
annualInterestRate = float(input('annualInterestRate = '))
monthlyPaymentRate = float(input('monthlyPaymentRate = '))

for month in range(12):
    balance = balance - balance * monthlyPaymentRate
    balance = balance + (annualInterestRate / 12) * balance
    # print('Month' + str(month + 1) + ' Remaining balance: ' + str(round(balance, 2)))

print('Remaining balance: ' + str(round(balance, 2)))
