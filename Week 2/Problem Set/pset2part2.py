# -*- coding: utf-8 -*-
"""
Created on 21/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

balance = float(input('Balance = '))
annualInterestRate = float(input('annualInterestRate = '))

monthlyInterestRate = annualInterestRate / 12.0
monthlyPayment = 10
auxBalance = balance

while auxBalance >= 0:
    auxBalance = balance
    for month in range(12):
        auxBalance -= monthlyPayment
        auxBalance += monthlyInterestRate * auxBalance
    if auxBalance <= 0:
        break
    else:
        monthlyPayment += 10

print('Lowest Payment: ' + str(monthlyPayment))
