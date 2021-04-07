# Henry Song  |  MA375  |  Spring 2021
# Project #1: Root-Finding Methods
# File: Secant.py
# Description: Method for Secant method. Default iteration is set to 1000.
#   - Inputs:(f, interval)
#   --- f: lambda representation of function
#   --- interval: array contanining search interval (i.e. [-2, 0])
#   - Output: approximation of root or None if DNE
#==========================================================================

def secant(f, interval):
    #separate the interval into corresponding a & b (looks simpler)
    a = interval[0]
    b = interval[1]

    #default iteration is set to 1000
    n = 1000

    #default error tolerance
    E = 0.000001

    #checks if a root exists by checking f(a)*f(b) (MUST be negative)
    if f(a)*f(b) >= 0: return None

    for i in range(n):
        # estimate for root
        xn = a - f(a)*(b - a)/(f(b) - f(a))
        
        if abs(f(xn)) > E:
            if f(xn) == 0: return xn, i    #found exact root
            #shifts variables 
            elif f(a)*f(xn) > 0: a = xn
            elif f(a)*f(xn) < 0: b = xn
            else: return None   #does not converge
        else:
            break
        # print statement used for testing
        # print("[", a, ", ", b , "]")
    return a - f(a)*(b - a)/(f(b) - f(a)), i