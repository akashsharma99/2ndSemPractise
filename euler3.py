from bisect import bisect_left
from math import sqrt
prime=[True] * 1000001
arr=[1] #list of all prime numbers till 10pow12
prime[0],prime[1]=False,False
#ensures that multiples of one are not
#traversed unlike previously where i had prime[1] as true
for p,pri in enumerate(prime):
    if (pri):
        arr.append(p)
        i=p*p
        while(i<=1000000):
            prime[i]=False
            i+=p

t = int(input())
for a0 in range(t):
    N = int(input())
    i = 2
    largest_prime=N
    while i <= int(sqrt(N)):
        while N % i == 0:
            largest_prime = i
            N //= i
        i += 1
    print(largest_prime)
