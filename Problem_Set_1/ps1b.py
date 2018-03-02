# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:49:32 2015

@author: Haley
"""

# Problem Set 1B
# Name: Haley Bates-Tarasewicz
# Collaborators: Katie Mathison
# Time spent: 0:10

# User input and variable declaration
s = float(raw_input('Enter the starting salary:')) 
p = float(raw_input('Enter the percent salary to save, as a decimal:'))
r = float(raw_input('Enter the annual raise, as a decimal:'))
n = 0

for year in range(45): # Loops for years in career
    
    for month in range(12): # loops for months per year
        n += ((n * .05) / 12) # Adds investments to nest egg
        n += ((s / 12) * p) # Adds savings to nest egg
    s += (s * r) # changes salary based on annual raise
    
print 'Retirement nest egg:', int(round(n))

