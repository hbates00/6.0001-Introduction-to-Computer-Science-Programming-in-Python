# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 17:26:18 2015

@author: Haley
"""

# Problem Set 1C
# Name: Haley Bates-Tarasewicz
# Collaborators: Katie Mathison
# Time spent: 1:00


# User input and variable declaration
starting = float(raw_input('Enter the starting salary:'))
s = starting 
rate = 5000
max = 10000 #upper bound of rate
min = 0 #lower bound of rate
count = 0
n = 0

# Loops while the nest egg isn't within the desired range
while not ((1999000) <= n <= (2001000)):
    # resets nest egg and starting salary for the next check    
    n = 0
    s = starting
    
    #finds n for a given rate
    for year in range(45):
    
        for month in range(12):
            n += ((n * .05) / 12)
            n += ((s / 12) * (rate / 10000.0))
        s += (s * .03)
    
    #checks if n is too small
    if n < 1999000:
        min = rate # sets the lower bound to the current rate
        rate = (rate + max) / 2 # sets rate to the average of rate and the upper bound
        count += 1 # increments rate
        
    elif n > 2001000:
        max = rate # sets the upper bound to the current rate
        rate = (rate + min) / 2 # sets rate to the average of rate and the lower bound
        count += 1 #increments count
        
    else:
        break

print 'Best savings rate:', (rate/10000.0)
print 'Steps in bisection search:', (count + 1)
        