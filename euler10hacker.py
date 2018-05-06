prime=[]

for i in range(1000001):
    prime.append(1)
p=2
while(p*p<=1000000):
    if (prime[p] == 1):
        i=p*p
        while(i<=1000000):
            prime[i]=0
            i+=p
    p+=1
def SumOfPrimes(n):
    s=0
    for i in range(2,n):
        if(prime[i]==1):
            s=s+i;
    print(s)

t = int(input())
for a0 in range(t):
    n = int(input())
    SumOfPrimes(n+1)
