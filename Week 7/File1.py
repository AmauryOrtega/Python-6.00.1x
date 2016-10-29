# -*- coding: utf-8 -*-
"""
Created on 29/10/2016

@author: Amaury Ortega <amauryocortega@gmail.com>
"""

import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i ** 2)
    myCubic.append(i ** 3)
    myExponential.append(1.5 ** i)

plt.figure('lin')  # Creates the figure because no figure names 'lin' has been created before
plt.xlabel('sample points')
plt.ylabel('linear function')
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.plot(myLinear, myQuadratic)
plt.figure('cube')
plt.plot(myLinear, myCubic)
plt.figure('expo')
plt.plot(myLinear, myExponential)

plt.figure('quad')
plt.ylabel('quadratic function')  # You can come back to a figure if you call it before

# Put titles
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')
plt.figure('cube')
plt.title('Cubic')
plt.figure('expo')
plt.title('Exponential')

# You can clear a figure
plt.figure('lin')
plt.clf()
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.plot(myLinear, myQuadratic)
plt.figure('cube')
plt.clf()
plt.plot(myLinear, myCubic)
plt.figure('expo')
plt.clf()
plt.plot(myLinear, myExponential)
# And then put titles
plt.figure('lin')
plt.title('Linear')
plt.figure('quad')
plt.title('Quadratic')
plt.figure('cube')
plt.title('Cubic')
plt.figure('expo')
plt.title('Exponential')

# Set Axis' limits
plt.figure('lin')
plt.clf()
plt.ylim(0, 1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.ylim(0, 1000)
plt.plot(myLinear, myQuadratic)
plt.figure('cube')
plt.clf()
plt.ylim(0, 1000)
plt.plot(myLinear, myCubic)
plt.figure('expo')
plt.clf()
plt.ylim(0, 1000)
plt.plot(myLinear, myExponential)

# Overlaying plots
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear)
plt.plot(myLinear, myQuadratic)
plt.figure('cube exp')
plt.clf()
plt.plot(myLinear, myCubic)
plt.plot(myLinear, myExponential)
# Titles
plt.figure('lin quad')
plt.title('Linear vs Quadratic')
plt.figure('cube exp')
plt.title('Cubic vs Exponential')

# Legends for plots
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, label='linear')
plt.plot(myLinear, myQuadratic, label='Quadratic')
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(myLinear, myExponential, label='exponential')
plt.legend()  # Takes the best location
plt.title('Cubic vs Exponential')

# More details
plt.figure('lin quad')
plt.clf()
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.plot(myLinear, myQuadratic, 'ro', label='Quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.plot(myLinear, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()  # Takes the best location
plt.title('Cubic vs Exponential')

# Subplots
plt.figure('lin quad')
plt.clf()
plt.subplot(211)  # Use 2 rows and 1 column, use the first position
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.subplot(212)  # Use 2 rows and 1 column, use the second position
plt.ylim(0, 900)
plt.plot(myLinear, myQuadratic, 'ro', label='Quadratic', linewidth=3.0)
plt.legend(loc='upper left')
plt.title('Linear vs Quadratic')

plt.figure('cube exp')
plt.clf()
plt.subplot(121)  # Use 1 rows and 2 column, use the first position
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.subplot(122)  # Use 1 rows and 2 column, use the second position
plt.ylim(0, 140000)
plt.plot(myLinear, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()  # Takes the best location
plt.title('Cubic vs Exponential')

# Scales
plt.figure('cube exp log')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=2.0)
plt.plot(myLinear, myExponential, 'r--', label='exponential', linewidth=4.0)
plt.yscale('log')
plt.legend()  # Takes the best location
plt.title('Cubic vs Exponential')

plt.figure('cube exp linear')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=2.0)
plt.plot(myLinear, myExponential, 'r--', label='exponential', linewidth=4.0)
plt.legend()  # Takes the best location
plt.title('Cubic vs Exponential')

plt.show()
