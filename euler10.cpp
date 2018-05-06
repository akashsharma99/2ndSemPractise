// C++ program to print all primes smaller than or equal to n using Sieve of Eratosthenes
#include <iostream>
#include<string.h>//for memset function to set memory to a particular value
using namespace std;

void SumOfPrimes(int n)
{
    bool prime[n+1];
    memset(prime, true, sizeof(prime));
    int s=0;
    for (int p=2; p*p<=n; p++)
    {
        if (prime[p] == true)
        {
            for (int i=p*p; i<=n; i += p)
                prime[i] = false;
        }
    }
    for(int i=2;i<=n;i++)
    {
          if(prime[i])
          s=s+i;
    }
    cout<<s<<endl;
}

// Driver Program to test above function
int main()
{
    int n;
    cout<<"Enter limit: ";
    cin>>n;
    SumOfPrimes(n);
    return 0;
}
