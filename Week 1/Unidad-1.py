# -*- coding: utf-8 -*-
"""
Created on 02/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

x = int(input('Ingrese un entero: '))

if x % 2 == 0:
    print('Par')
else:
    print('Impar')
print('Termino')

print('')
if x % 2 == 0:
    if x % 3 == 0:
        print('Divisible por 2 y 3')
    else:
        print('Divisible por 2 y no por 3')
elif x % 3 == 0:
    print('Divisible por 3 y no por 2')

"""
Prioridad de operadores logicos
()
not
and
or
"""