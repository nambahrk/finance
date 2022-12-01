import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

K=100
r=0.01
q=0.03
tend=1
t=0
sig=0.2

x = np.empty(0)
y1 = np.empty(0)
y2 = np.empty(0)
y3 = np.empty(0)
y4 = np.empty(0)
y5 = np.empty(0)
y6 = np.empty(0)
y7 = np.empty(0)

for i in range(0,150):
    S=i+50 #株価
    d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
    d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

    call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
    x= np.append(x, S)
    y1= np.append(y1, call)

for i in range(0,150):
    SS=i+50
    n=10
    deltat=tend/n
    #上昇下降
    u=math.exp(sig*math.sqrt(3*deltat))
    d=math.exp(-sig*math.sqrt(3*deltat))
    #確率
    pu=1/6+(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    pm=2/3
    pd=1/6-(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    call = np.zeros((n+1, 2*n+1)) #リスト何個、リストの要素何個
    for i in range(-n,n+1): #-n～n
        S = u**(i)*SS
        #S=SS*math.exp((r-q-sig**2/2)*tend+sig*math.sqrt(tend)*random.gauss(0,1))
        C=max(S-K,0)
        call[n][n-i]=C #どのリストの何番目

    for i in range(n,0,-1):  #1～n(時間軸)
        k=2*i-1 #k=2n-1～1()
        for j in range(1,k+1): #(推移)
            call[i-1][j-1]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
            #call[i-1][j]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
    y2= np.append(y2, call[0][0])

for i in range(0,150):
    SS=i+50
    n=50
    deltat=tend/n
    #上昇下降
    u=math.exp(sig*math.sqrt(3*deltat))
    d=math.exp(-sig*math.sqrt(3*deltat))
    #確率
    pu=1/6+(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    pm=2/3
    pd=1/6-(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    call = np.zeros((n+1, 2*n+1)) #リスト何個、リストの要素何個
    for i in range(-n,n+1): #-n～n
        S = u**(i)*SS
        #S=SS*math.exp((r-q-sig**2/2)*tend+sig*math.sqrt(tend)*random.gauss(0,1))
        C=max(S-K,0)
        call[n][n-i]=C #どのリストの何番目

    for i in range(n,0,-1):  #1～n(時間軸)
        k=2*i-1 #k=2n-1～1()
        for j in range(1,k+1): #(推移)
            call[i-1][j-1]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
            #call[i-1][j]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
    y3= np.append(y3, call[0][0])

for i in range(0,150):
    SS=i+50
    n=200
    deltat=tend/n
    #上昇下降
    u=math.exp(sig*math.sqrt(3*deltat))
    d=math.exp(-sig*math.sqrt(3*deltat))
    #確率
    pu=1/6+(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    pm=2/3
    pd=1/6-(r-sig*sig/2)*math.sqrt(deltat/12/sig**2)
    call = np.zeros((n+1, 2*n+1)) #リスト何個、リストの要素何個
    for i in range(-n,n+1): #-n～n
        S = u**(i)*SS
        #S=SS*math.exp((r-q-sig**2/2)*tend+sig*math.sqrt(tend)*random.gauss(0,1))
        C=max(S-K,0)
        call[n][n-i]=C #どのリストの何番目

    for i in range(n,0,-1):  #1～n(時間軸)
        k=2*i-1 #k=2n-1～1()
        for j in range(1,k+1): #(推移)
            call[i-1][j-1]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
            #call[i-1][j]=math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1])
    y4= np.append(y4, call[0][0])


y5=y2-y1
y6=y3-y1
y7=y4-y1


fig = plt.figure(figsize=(10, 5))
ax=fig.subplots()
ax.set_xlabel("stock price(yen)")
ax.set_ylabel("delta call(yen)")
ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend)+ ',sigma=' + str(sig))
plt.plot(x, y5, label="n=10")
plt.plot(x, y6 ,label="n=50")
plt.plot(x, y7 ,label="n=200")
plt.legend()
plt.savefig("a.jpg")
plt.show()
