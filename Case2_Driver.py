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
diff_start_time = time.time()
f_prime = sym.lambdify(r, sym.diff(equation))   #lambda representation of derivative of equation
diff_time = time.time() - diff_start_time

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
print("Fastest to slowest times\t\t\tFastest to slowest iterations")
bool1 = bool2 = bool3 = bool4 = False
sorted_times = sorted([execution_time1, execution_time2, execution_time3, execution_time4])
sorted_iterations = sorted([bisection_result[1], newton_result[1], secant_result[1], falsi_result[1]])
#print(criteria)
for i in range(len(sorted_times)):
    print(i+1, ":", end=" ")
    if sorted_times[i] == execution_time1: print("Bisection Method", end="\t\t\t\t")
    elif sorted_times[i] == execution_time2: print("Newton's Method", end="\t\t\t\t")
    elif sorted_times[i] == execution_time3: print("Secant Method", end="\t\t\t\t")
    elif sorted_times[i] == execution_time4: print("Falsi Method", end="\t\t\t\t")

    print(i+1, ":", end=" ")
    if sorted_iterations[i] == bisection_result[1] and bool1 == False: 
        print("Bisection Method")
        bool1 = True
    elif sorted_iterations[i] == newton_result[1] and bool2 == False: 
        print("Newton's Method")
        bool2 = True
    elif sorted_iterations[i] == secant_result[1] and bool3 == False: 
        print("Secant Method")
        bool3 = True
    elif sorted_iterations[i] == falsi_result[1] and bool4 == False: 
        print("Falsi Method")
        bool4 = True

print()