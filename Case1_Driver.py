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

interval = [499, 500]

print()
print("MA375 - Project #1")
print("Case #1")
print()

start_time1 = time.time()
print("Bisection Method over interval", interval ,"\t:\t", bisection(f, interval))
print("Execution time in seconds: ", "{:.8f}".format(time.time()-start_time1))

print()

start_time2 = time.time()
print("Newton's Method over interval", interval ,"\t:\t", newton(f, f_prime, 499))
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