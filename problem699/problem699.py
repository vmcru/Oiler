'''
<p>
Let $\sigma(n)$ be the sum of all the divisors of the positive integer $n$, for example:<br />
$\sigma(10) = 1+2+5+10 = 18$.
</p>
<p>
Define $T(N)$ to be the sum of all numbers $n \le N$ such that when the fraction $\frac{\sigma(n)}{n}$ is written in its lowest form $\frac ab$, the denominator is a power of 3 i.e. $b = 3^k, k &gt; 0$.
</p>
<p>
You are given $T(100) = 270$ and $T(10^6) = 26089287$.
</p>
<p>
Find $T(10^{14})$.
</p>
'''
from math import log


def is_a_power_of(n,p):
    '''function that checks if a given number n is a power of p'''
    k = log(n)/log(p)
    if k- int(p) == 0:
        return True
    else:
        return False 

def sigma(n: int)->int:
    ''' function that generates the sum of the divisors of the number n'''
    collection = {}
    for i in range(n):
        if n/i -int(n/i) == 0:
            collection[n]= i
            collection[i] = n
    
    return 0


def main()-> int:
    return 0

if __name__ == "__main__":
    print(main())