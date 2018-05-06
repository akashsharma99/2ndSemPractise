prime=[1] * 1000001
arr=[]
prime[0],prime[1]=0,0
#ensures that multiples of one are not traversed unlike previously where i had prime[1] as true
for p,pri in enumerate(prime):
    if (pri):
        arr.append(p)
        i=p*p
        while(i<=1000000):
            prime[i]=0
            i+=p

t = int(input())
for a0 in range(t):
    n = int(input())
    print(arr[n-1])
