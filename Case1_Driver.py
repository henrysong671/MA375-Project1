from Bisection import bisection
from Newton import newton
from Secant import secant
from Falsi import falsi
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib
import time

a = sym.symbols('a')
equation = 500*sym.tan(a)-(32.2/(2*(1500**2)*(sym.cos(a)**2)))*500**2-50
f = sym.lambdify(a, equation)
f_prime = sym.lambdify(a, sym.diff(equation))

interval = [499, 501]

print()
print("MA375 - Project #1")
print("Case #1")
print()
print("f(a) = ", equation)
print("Interval = ", interval)
print()

start_time1 = time.time()
print("Bisection Method over interval", interval ,"\t:\t", bisection(f, interval))
execution_time1 = time.time()-start_time1
print("Execution time in seconds: ", "{:.8f}".format(execution_time1))

print()

start_time2 = time.time()
print("Newton's Method over interval", interval ,"\t:\t", newton(f, f_prime, 501))
execution_time2 = time.time()-start_time2
print("Execution time in seconds: ", "{:.8f}".format(execution_time2))

print()

start_time3 = time.time()
print("Secant Method over interval", interval ,"\t\t:\t", secant(f, interval))
execution_time3 = time.time()-start_time3
print("Execution time in seconds: ", "{:.8f}".format(execution_time3))

print()

start_time4 = time.time()
print("Falsi Method over interval", interval ,"\t\t:\t", falsi(f, interval))
execution_time4 = time.time()-start_time4
print("Execution time in seconds: ", "{:.8f}".format(execution_time4))

print()

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