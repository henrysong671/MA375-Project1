from Bisection import bisection
from Newton import newton
from Secant import secant
from Falsi import falsi
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt
import matplotlib
import time

r = sym.symbols('r')
equation = 80-20*sym.log(r, 10)-0.00115*r-10
f = sym.lambdify(r, equation)
f_prime = sym.lambdify(r, sym.diff(equation))

interval = [79, 81]

print()
print("MA375 - Project #1")
print("Case #2")
print()
print("f(a) = ", equation)
print("Interval = ", interval)
print()

start_time1 = time.time()
print("Bisection Method over interval", interval ,"\t:\t", bisection(f, interval))
print("Execution time in seconds: ", "{:.8f}".format(time.time()-start_time1))

print()

start_time2 = time.time()
print("Newton's Method over interval", interval ,"\t:\t", newton(f, f_prime, 500))
print("Execution time in seconds: ", "{:.8f}".format(time.time()-start_time2))

print()

start_time3 = time.time()
print("Secant Method over interval", interval ,"\t\t:\t", secant(f, interval))
print("Execution time in seconds: ", "{:.8f}".format(time.time()-start_time3))

print()

start_time4 = time.time()
print("Falsi Method over interval", interval ,"\t\t:\t", falsi(f, interval))
print("Execution time in seconds: ", "{:.8f}".format(time.time()-start_time4))

print()