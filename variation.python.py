from sympy import*
x=symbols('x')
y,f=symbols('y,f',cls=Function)
f=lambda y,x: y (x)**2+diff(y(x),x)**2+2*y(x)*exp(x)
eq=diff(f(y, x),y(x))-diff(f(y,x),diff(y(x)),x)
soln=dsolve(eq,y(x))
pprint(expand(soln))
