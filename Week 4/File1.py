# -*- coding: utf-8 -*-
"""
Created on 28/09/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""
'''
Defensive programming:
    docstring = specifications for functions
    modularize = split program in functions
    check conditions on input/output

Testing/Validation:
    prepare input and output to check program
    how can i break my program

Debugging:
    which events leads to the error
    why is not working?
    how can i fix it?

Setup for testing and debugging:
    break program into modules
    document constraints = docstring on modules

Testing:
    ensure code runs
    expected result to some inputs

    types:
        unit testing
        regression testing = check previous bugs in the same function
        integration testing = whole program

Runtime bugs:
Overt vs covert
    Overt = crashes or infinite loop
    Covert = returns incorrect value
Persistent vs intermittent:
    Persistent = occurs every time
    Intermittent = only some times, even with same input
'''

# Exceptions
try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print(a / b)
    print("Okay")
except:
    print("Bug in user input.")
print("Outside")

try:
    a = int(input("Tell me one number:"))
    b = int(input("Tell me another number:"))
    print('a / b =', a / b)
    print('a + b =', a + b)
except ValueError:
    print('Could not convert to number')
except ZeroDivisionError:
    print("Can't divide by 0")
except:
    print('Something went very wrong')
else:
    # If try body runs okay, this is executed
    print('Else body')
finally:
    # Always runs after try, else, except, break, continue or return
    print('Finally body')

# Handle input
while True:
    try:
        n = input('Please enter an integer: ')
        n = int(n)
        break
    except ValueError:
        print('Input not an integer; try again')
print('Correct input of an integer')

# Handle files
data = []
file_name = input('Provide a file name for data')

try:
    file_handler = open(file_name, 'r')
except IOError:
    print('Cannot open', file_name)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',')  # Remove tailing \n
            data.append(addIt)
finally:
    file_handler.close()
