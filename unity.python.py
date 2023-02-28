G = {0,1,2,3,4,5,6}
def f(a,b):
 return (a*b)%7
for a in G:
    k=0
    for b in G:
        if f(a,b) == b and f(b,a) == b:
             e=a
             k+=1
    if k==len(G):
        print(e,'is the multiplicative identity and the ring is with unity')
        break
else:
     print('Multiplicative identity does not exists, hence given ring is without unity')
