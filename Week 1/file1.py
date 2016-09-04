# -*- coding: utf-8 -*-
"""
Created on 02/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

x = int(input('Enter an integer: '))

if x % 2 == 0:
    print('Even')
else:
    print('Odd')
print('End')

print('')
if x % 2 == 0:
    if x % 3 == 0:
        print('/ by 2 and 3')
    else:
        print('/ by 2 and not by 3')
elif x % 3 == 0:
    print('/ by 3 y not by 2')

"""
Priority of logic operators
()
not
and
or
"""
