import numpy
from sympy import symbols, solve

#04.28=8.03+a+b
#-9.54=-1.4*8.03-1.1*b+0.2
#b?a?

#x=Symbol('x')
#equation = 2 * x - 6
#print(solve(equation))

o, b =symbols('o,b')
equation1 = 8.03 + o + b-4.28
equation2 = (-1.4*8.03)-(1.1*b)+0.2+9.54
print(solve((equation2,equation1)))
