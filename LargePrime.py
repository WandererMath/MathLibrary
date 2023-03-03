from random import randint
from time import time

def prime(N):
    N=N-2
    A=2
    P=[]
    P.append(A)
    A=3
    P.append(A)
    while A<=N:
        A=A+2
        t=2+N**0.5
        t=int(t)
        for p in P:
            if p>t:
                break
            if A%p==0:
                break
        if A%p==0:
            continue
        P.append(A)
    return P

prime100=prime(100)

def No_2(N):
    i=0
    while N%2==0:
        i+=1
        N//=2
    return i, N

def Rabin(p, a):
    n=p-1
    t, m=No_2(n)
    result=pow(a, m, p)
    if result==1 or result==p-1:    return True
    i=0
    while i<t-1:
        result=pow(result, 2, p)
        if result==1:   return False
        if result==p-1:  return True
        i+=1
    return False



def n_random(r, n):  #from 2 to r-1
    result=[]
    i=0
    while i<n:
        a=randint(2, r-1)
        if  not a in result:
            result.append(a)
            i+=1
    return result

def prime_test(p, n=5):#p should > 100
    for i in prime100:
        if p%i==0:  return False
    #rands=n_random(p, n)
    rands=[2,3,4,5,6]
    for i in rands:
        if not Rabin(p, i): return False
    return True     


def generate_prime(a=10, b=16):
    x=randint(10**a, 10**b)
    if x%2==0:
        x+=1
    while not prime_test(x):
        x+=2
        #print(x, False)
    return x


#for i in range(5):
    #print(prime_test(int(input())))
if __name__=='__main__':
    t=time()
    for i in range(5):
        print(generate_prime(200,250),'\n')
    print(time()-t)

