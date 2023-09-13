###Look back option###

import random
import numpy as np
import matplotlib.pyplot as plt

#with fixed strike   
def call_lookback(S=100, K=110, r=0.01, sig=0.2, T=1, n=10000, M=100):
    dt=T/M
    call_price = 0
    for i in range(n):   
        Smax=S          
        Stmp=S
        for j in range(M):
            epsilon=np.random.normal(0,1,M)
            Stmp = Stmp*np.exp((r-0.5*sig**2)*dt+sig*np.sqrt(dt)*epsilon[j])
            if Smax < Stmp:
                Smax = Stmp
        call_price += max(Smax-K,0)
    call_price = np.exp(-r*T)*call_price/n    
    return call_price

#with floating strike
def call_lookback(S=100, K=110, r=0.01, sig=0.2, T=1, n=10000, M=100):
    dt=T/M
    call_price = 0
    for i in range(n):   
        Smin=S          
        Stmp=S
        for j in range(M):
            epsilon=np.random.normal(0,1,M)
            Stmp = Stmp*np.exp((r-0.5*sig**2)*dt+sig*np.sqrt(dt)*epsilon[j])
            if Smin > Stmp:
                Smin = Stmp
        call_price += Stmp-Smin
    call_price = np.exp(-r*T)*call_price/n    
    return call_price


#with fixed strike    
def put_lookback(S=100, K=110, r=0.01, sig=0.2, T=1, n=10000, M=100):
    dt=T/M
    put_price = 0
    for i in range(n):   
        Smin=S          
        Stmp=S
        for j in range(M):
            epsilon=np.random.normal(0,1,M)
            Stmp = Stmp*np.exp((r-0.5*sig**2)*dt+sig*np.sqrt(dt)*epsilon[j])
            if Smin > Stmp:
                Smin = Stmp
        put_price += max(K-Smin,0)
    put_price = np.exp(-r*T)*put_price/n    
    return put_price


#with floating strike
def put_lookback2(S=100, K=110, r=0.01, sig=0.2, T=1, n=10000, M=100):
    dt=T/M
    put_price = 0
    for i in range(n):   
        Smax=S          
        Stmp=S
        for j in range(M):
            epsilon=np.random.normal(0,1,M)
            Stmp = Stmp*np.exp((r-0.5*sig**2)*dt+sig*np.sqrt(dt)*epsilon[j])
            if Smax < Stmp:
                Smax = Stmp
        put_price += Smax-Stmp
    put_price = np.exp(-r*T)*put_price/n  
    return put_price

#with fixed strike (with MC loop figure)   
def put_lookback3(S=100, K=110, r=0.01, sig=0.2, T=1, n=10000, M=100):
    dt=T/M
    put_price = 0
    list_x = np.empty(0)    
    list_put = np.empty(0)    
    for i in range(n):   
        Smin=S          
        Stmp=S
        for j in range(M):
            epsilon=np.random.normal(0,1,M)
            Stmp = Stmp*np.exp((r-0.5*sig**2)*dt+sig*np.sqrt(dt)*epsilon[j])
            if Smin > Stmp:
                Smin = Stmp
        put_price += max(K-Smin,0)
        list_put = np.append(list_put,np.exp(-r*T*(i+1)/n)*put_price/(i+1))
        list_x   = np.append(list_x, i+1)
    
    plt.plot(list_x, list_put)
    plt.xlabel("loop")
    plt.ylabel("Look Back Put Option Price")
    plt.savefig("loop_put.png")
    plt.show()


#print(call_lookback(100, 80, 0.02, 0.1, 1, 10000, 100))
#print(put_lookback(100, 110, 0.01, 0.2, 1, 1000, 100))
put_lookback3(100, 110, 0.01, 0.2, 1, 3000, 100)
