from math import*
a= int(input ("Enter the lower limit: "))
b= int (input ("Enter the upper limit: "))
n= int(input("Enter the length: "))
def f(x):
    return 1/(1+x**2)
def simpson38 (a,b,n):
    h= (b-a)/n
    sum=f(a) + f(b)
    for i in range (1,n):
        c = a+i*h
        if i%3==0:
            sum+=2*f(c)
        else:
            sum+=3*f (c)
    S38=(3*h/8)*sum
    return S38
result=simpson38 (a, b, n)
print ("Result by Simpson's 38 Rule is: ", result)
