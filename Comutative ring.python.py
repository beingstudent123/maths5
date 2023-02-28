G = {0,2,4,6,8}
def f(a,b):
 return (a*b)%10
for a in G:
    for b in G:
     if f(a,b)!=f(b,a):
        print("Ring is not commutative")
        break
else:
 print("Ring is commutative")

