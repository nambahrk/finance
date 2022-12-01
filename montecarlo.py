import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import norm

S=K=100 #権利行使価格
r=0.01 #リスクフリーレート
q=0.03 #金利
tend=1 #満期
t=0 #時間
sig=0.2 #ボラティリティ
m=100 #分割
n=100000 #simulation数

x1 = np.empty(0)
y1 = np.empty(0)
sample = np.empty(0)
sample2 = np.empty(0)
call = np.empty(0)
call_bs = np.empty(0)

'''
for i in range(1,n+1): #1-nのループ
    #sample=np.append(sample,sample[i-1]+r*sample[i-1]*deltat+sig*sample[i-1]*math.sqrt(deltat)*random.gauss(0,1))
    #sample = np.append(sample, sample[i-1]*math.exp((r-q-sig*sig/2)*deltat+sig*np.sqrt(deltat)*random.gauss(0,1)))
    rand=max(0, sample[i]-K)

    #SS=S*math.exp((r-q-sig*sig/2)*tend/n+sig*np.sqrt(tend/n)*random.gauss(0,1))
    #rand=max(0, SS-K)

    sample2 = np.append(sample2, rand)
    price = math.exp(-r*deltat)*(sum(sample2))/i
    y1= np.append(y1, price)
'''

for j in range(n):
    #sample = np.append(sample, S)
    #for i in range(m):

    #    sample=np.append(sample, sample[i-1]+(r-q)*sample[i-1]*(tend/m)+sig*sample[i-1]*math.sqrt(tend/m)*random.gauss(0,1))

    #sample2=np.append(sample2, max(sample[m]-K,0))
    #sample = np.empty(0)

    sample = S*np.exp((r-q-sig*sig/2)*tend+sig*random.gauss(0,1)*np.sqrt(tend))
    sample2=np.append(sample2, max(sample-K,0))

    call=np.append(call, math.exp(-r*tend)*sum(sample2)/j)

    d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
    d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
    call_bs = np.append(call_bs, S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1))


x1= np.append(x1, list(range(1,n+1)))
fig = plt.figure(figsize=(10, 5))
ax=fig.subplots()
plt.plot(x1, call)
plt.plot(x1, call_bs)
ax.set_xlabel("times")
ax.set_ylabel("call(yen)")
ax.set_title('r=' + str(r) + ', S=K=' + str(K) + ',sigma=' + str(sig) + ',T=' + str(tend)  + ',q=' + str(q))
plt.legend()
plt.savefig("a.jpg")
plt.show()
