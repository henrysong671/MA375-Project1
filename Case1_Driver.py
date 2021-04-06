# Henry Song  |  MA375  |  Spring 2021
# Project #1: Root-Finding Methods
# File: Case1_Driver.py
# Description: Runs the driver code (containing all 4 methods) for Case #1
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

# Function definitions
a = sym.symbols('a')    # define a as a variable (needed for lambda function)
equation = 500*sym.tan(a)-(32.2/(2*(1500**2)*((sym.cos(a))**2)))*500**2-50    # equation that will be used for root-finding methods
f = sym.lambdify(a, equation)   #lambda representation of equation
diff_start_time = time.time()
f_prime = sym.lambdify(a, sym.diff(equation))   #lambda representation of derivative of equation
diff_time = time.time() - diff_start_time

# interval definition
interval = [5.5, 6.5]

print()
print("MA375 - Project #1")
print("Case #1")
print()
print("f(a) = ", equation)
print("Interval = ", interval)
print()

print("**Note: Interval and values are provided and given in Radians")
#   1. Bisection Method
start_time1 = time.time()   # start time
bisection_result = bisection(f, interval)   # runs bisection method
print("Bisection Method over interval", interval ,"\t:\t", bisection_result[0], "in", bisection_result[1], "iterations.")  
execution_time1 = time.time()-start_time1   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time1))

print()

#   2. Newton's Method
start_time2 = time.time()   # start time
newton_result = newton(f, f_prime, interval)     # runs Newton's Method
print("Newton's Method over interval", interval ,"\t:\t", newton_result[0], "in", newton_result[1], "iterations using estimate: ", newton_result[2], ".")  
execution_time2 = time.time()-start_time2   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time2))
print("Execution time including differentiation: ", "{:.8f}".format(execution_time2+diff_time))

print()

#   3. Secant Method
start_time3 = time.time()   # start time
secant_result = secant(f, interval)     # runs secant method
print("Secant Method over interval", interval ,"\t\t:\t", secant_result[0], "in", secant_result[1], "iterations.")  
execution_time3 = time.time()-start_time3   # calculates time to execute method
print("Execution time in seconds: ", "{:.8f}".format(execution_time3))

print()

#   4. Falsi Method
start_time4 = time.time()   # start time
falsi_result = falsi(f, interval)   # runs falsi method
print("Falsi Method over interval", interval ,"\t\t:\t", falsi_result[0], "in", falsi_result[1], "iterations.")    
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