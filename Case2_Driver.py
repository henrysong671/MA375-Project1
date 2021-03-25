# Henry Song  |  MA375  |  Spring 2021
# Project #1: Root-Finding Methods
# File: Case2_Driver.py
# Description: Runs the driver code (containing all 4 methods) for Case #2
#==========================================================================

from Bisection import bisection
from Newton import newton
from Secant import secant
from Falsi import falsi
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib
import time

# function definitions
r = sym.symbols('r')    # define r as a variable (needed for lambda function)
equation = 80-20*sym.log(r, 10)-0.00115*r-20    # equation that will be used for root-finding methods
f = sym.lambdify(r, equation)   #lambda representation of equation
f_prime = sym.lambdify(r, sym.diff(equation))   #lambda representation of derivative of equation

# interval definition
interval = [888, 889]

print()
print("MA375 - Project #1")
print("Case #2")
print()
print("f(a) = ", equation)
print("Interval = ", interval)
print()

#   1. Bisection Method
start_time1 = time.time()   # start time
print("Bisection Method over interval", interval ,"\t:\t", bisection(f, interval))  # runs bisection method
execution_time1 = time.time()-start_time1   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time1))

print()

#   2. Newton's Method
start_time2 = time.time()   # start time
print("Newton's Method over interval", interval ,"\t:\t", newton(f, f_prime, 888))  # runs Newton's Method
execution_time2 = time.time()-start_time2   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time2))

print()

#   3. Secant Method
start_time3 = time.time()   # start time
print("Secant Method over interval", interval ,"\t\t:\t", secant(f, interval))  # runs secant method
execution_time3 = time.time()-start_time3   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time3))

print()

#   4. Falsi Method
start_time4 = time.time()   # start time
print("Falsi Method over interval", interval ,"\t\t:\t", falsi(f, interval))    # runs falsi method
execution_time4 = time.time()-start_time4   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time4))

print()

# sorts and prints methods from fastest execution time to slowest
print("Fastest to slowest methods:")
sorted_times = sorted([execution_time1, execution_time2, execution_time3, execution_time4])
counter = 1
for i in sorted_times:
    print(counter, ":", end=" ")
    if i == execution_time1: print("Bisection Method")
    elif i == execution_time2: print("Newton's Method")
    elif i == execution_time3: print("Secant Method")
    elif i == execution_time4: print("Falsi Method")
    counter += 1

print()