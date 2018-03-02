# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:56:56 2015

@author: Haley
"""

# Problem Set 1A
# Name: Haley Bates-Tarasewicz
# Collaborators: Katie Mathison
# Time spent: 0:20

# User input and variable declaration
s = float(raw_input('Enter the starting salary:')) 
p = float(raw_input('Enter the percent salary to save, as a decimal:'))
n = 0

# Start of loop for entire career
for year in range(45): # Loops for years in career

    for month in range(12): # loops for months per year
        n += ((n * .05) / 12) # Adds investments to nest egg
        n += ((s / 12) * p) # Adds savings to nest egg
    
print 'Retirement nest egg:', int(round(n))

