def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
        
print(gcd(30,20))
def pollard(n):
    a = 2
    count = 2
    for j in range(3,102):
        t = pow(a,count,n)
        g = gcd(t-1,n)
        if g > 1 and g < n:
            return g
        count *= j
print(pollard(168441398857))
        
        