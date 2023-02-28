from numpy import*
a=0  #Lower limit
b=1  #Upper limit
p=6 #Number of equal parts
n=7 #Number of Ordinates (n=p+1)
h=(b-a)/p
x=linspace (a,b,n)
f=1/(1+x)
for i in range (0,n):
    print (round (f[i],ndigits=4))
TR=round((h/2)* (f[0]+2*sum (f[1:n-1])+f[n-1]), ndigits=4)
print ("The required integral by Trapezoidal Rule is", TR)
