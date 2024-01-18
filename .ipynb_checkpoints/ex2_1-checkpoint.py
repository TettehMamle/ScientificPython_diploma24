import math
import sympy as sp
import numpy as np

def function(n):
    h = sp.symbols('h')
    x = sp.symbols('x')
    i = 0
    expr = 0
    for i in range(n):
        expr = expr + ((-h +x)**i/math.factorial(i))*sp.diff(sp.sin(x),x,i).subs(x,h)
     
    #return function(n)
    return expr
sp.init_printing(order='rev-lex')   
function(5)
print(function(5))

h = sp.symbols('h')
x = sp.symbols('x')
print(sp.sin(x).series(x,h, n=5))
