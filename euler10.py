def SumOfPrimes(n):
    prime=[]
    for i in range(n+1):
        prime.append(1)
    s=0
    p=2
    while(p*p<=n):
        if (prime[p] == 1):
                i=p*p
                while(i<=n):
                    prime[i]=0
                    i+=p
        p+=1
    for i in range(2,n):
        if(prime[i]==1):
            s=s+i;
    print(s)

n=int(input("Enter limit"))
SumOfPrimes(n);
