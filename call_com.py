import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.stats import norm

K=100 #権利行使価格
r=0.1 #リスクフリーレート
q=0.3 #金利
tend=1 #満期
t=0 #時間
sig=0.2#ボラティリティ

x1 = np.empty(0)
y1 = np.empty(0)
x2 = np.empty(0)
y2 = np.empty(0)

#よーろ
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
    x1= np.append(x1, SS)
    y1= np.append(y1, call[0][0])


#アメリカ
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
    st=np.empty(0)
    for i in range(-n,n+1): #-n～n
        S = u**(i)*SS
        #S=SS*math.exp((r-q-sig**2/2)*tend+sig*math.sqrt(tend)*random.gauss(0,1))
        #st=np.append(st,S)
        C=max(S-K,0)
        call[n][n-i]=C #どのリストの何番目

    for i in range(n,0,-1):  #1～n(時間軸)
        k=2*i-1 #k=2n-1～1()
        for j in range(1,k+1): #(推移)
            call[i-1][j-1]=max(math.exp(-r*deltat)*(pu*call[i][j+1]+pm*call[i][j]+pd*call[i][j-1]), SS*u**(-j)-K)
    x2= np.append(x2, SS)
    y2= np.append(y2, call[0][0])

fig = plt.figure(figsize=(10, 5))
ax=fig.subplots()
plt.plot(x1, y1,label="European")
plt.plot(x2, y2,label="American")
ax.set_xlabel("stock price(yen)")
ax.set_ylabel("call(yen)")
ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',T=' + str(tend)  + ',q=' + str(q))
plt.legend()
plt.savefig("a.jpg")
plt.show()
