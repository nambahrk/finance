import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import norm

S=K=100 #strike
r=0.01 #risk free rate
q=0.03 #interest
tend=1 #maturity
t=0 #time
sig=0.2 #volatility
m=100 #divide
n=100000 #number of simulation

x1,y1,sample,sample2,call,call_bs = np.empty(0)

d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
call_bs = np.append(call_bs, S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1))

for j in range(n):
    sample = S*np.exp((r-q-sig*sig/2)*tend+sig*random.gauss(0,1)*np.sqrt(tend))
    sample2=np.append(sample2, max(sample-K,0))
    call=np.append(call, math.exp(-r*tend)*sum(sample2)/j-call_bs)


x1= np.append(x1, list(range(1,n+1)))
fig = plt.figure(figsize=(10, 5))
ax=fig.subplots()
plt.bar(x1, call)
ax.set_xlabel("times")
ax.set_ylabel("delta")
ax.set_ylim([-1,3])
ax.set_title('r=' + str(r) + ', S=K=' + str(K) + ',sigma=' + str(sig) + ',T=' + str(tend)  + ',q=' + str(q))
plt.legend()
plt.savefig("a.jpg")
plt.show()
