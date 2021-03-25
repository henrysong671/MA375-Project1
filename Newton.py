# Henry Song  |  MA375  |  Spring 2021
# Project #1: Root-Finding Methods
# File: Newton.py
# Description: Method for Newton's method. Default iteration is set to 1000.
#   - Inputs:(f, interval, x0)
#   --- f: lambda representation of function
#   === f_prime: lambda representation of derivitive of function
#   --- interval: array contanining search interval (i.e. [-2, 0])
#   - Output: approximation of root or None if DNE
#==========================================================================
import random
def newton(f, f_prime, interval):
    # default iteration is set to 1000
    n = 1000

    # default error tolerance is set to 0.000001
    E = 0.000001

    x0 = interval[0]#random.uniform(float(interval[0]), float(interval[1]))
    original_x0 = x0

    r = x0 - f(x0)/f_prime(x0)

    for i in range(n):
        # checks if root falls into error tolerance
        if abs(r) >= E and abs(x0) >= E: 
            # checks if |f(x0)| < E
            if abs(f(x0)) < E: return x0, i, original_x0

            xn = x0
            x0 = x0 - f(x0)/f_prime(x0)

            # checks if |xn-x| < E
            if abs(xn - x0) < E: return x0, i, original_x0
        else:
            break
    return r, i, original_x0