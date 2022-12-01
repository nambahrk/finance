import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm


def default():
    K=100
    r=0.01
    q=0.03
    tend=1
    t=0
    sig=0.2

    return K,r,q,tend,t,sig

#時間依存性を見る(株価Sも変える)
#権利行使価格,リスクフリーレート,配当利回り,初期時間,ボラティリティ
def time():
    x = np.empty(0)
    y1 = np.empty(0)
    y2 = np.empty(0)
    y3 = np.empty(0)
    y4 = np.empty(0)
    y5 = np.empty(0)
    y6 = np.empty(0)
    y7 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,100):
        S=90
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        x= np.append(x, tend)
        y1= np.append(y1, call)

    for i in range(1,100):
        S=95
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y2= np.append(y2, call)

    for i in range(1,100):
        S=100
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y3= np.append(y3, call)

    for i in range(1,100):
        S=105
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y4= np.append(y4, call)

    for i in range(1,100):
        S=110
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y5= np.append(y5, call)

    for i in range(1,100):
        S=115
        tend=i/100 #時間
        d1=(math.log(S/K)+(r+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y6= np.append(y6, call)

    return x,y1,y2,y3,y4,y5,y6

def plot_time(x,y1,y2,y3,y4,y5,y6):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("time(yr)")
    ax.set_ylabel("call(yen)")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',q=' + str(q))
    #ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))

    plt.plot(x, y1, label="S=90")
    plt.plot(x, y2, label="S=95")
    plt.plot(x, y3, label="S=100")
    plt.plot(x, y4, label="S=105")
    plt.plot(x, y5, label="S=110")
    plt.plot(x, y6, label="S=115")
    plt.legend()
    #plt.plot(x2, y2, color = 'blue', marker = 'v')
    plt.savefig("a.jpg")
    plt.show()



#risk依存性を見る(株価も変える)
#権利行使価格,配当利回り,期間,初期時間,ボラティリティ
def risk():
    x = np.empty(0)
    y1 = np.empty(0)
    y2 = np.empty(0)
    y3 = np.empty(0)
    y4 = np.empty(0)
    y5 = np.empty(0)
    y6 = np.empty(0)
    y7 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,100):
        S=85
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        x= np.append(x, r)
        y1= np.append(y1, call)

    for i in range(1,100):
        S=90
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y2= np.append(y2, call)

    for i in range(1,100):
        S=95
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y3= np.append(y3, call)

    for i in range(1,100):
        S=100
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y4= np.append(y4, call)

    for i in range(1,100):
        S=105
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y5= np.append(y5, call)

    for i in range(1,100):
        S=110
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y6= np.append(y6, call)

    for i in range(1,100):
        S=115
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y7= np.append(y7, call)
    return x,y1,y2,y3,y4,y5,y6,y7


def plot_risk(x,y1,y2,y3,y4,y5,y6,y7):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("risk free rate")
    ax.set_ylabel("call(yen)")
    ax.set_title('K=' + str(K) + ',q=' + str(q) + ',T=' + str(tend) + ',sigma=' + str(sig) )
    plt.plot(x, y1, label="S=85")
    plt.plot(x, y2, label="S=90")
    plt.plot(x, y3, label="S=95")
    plt.plot(x, y4, label="S=100")
    plt.plot(x, y5, label="S=105")
    plt.plot(x, y6, label="S=110")
    plt.plot(x, y7, label="S=115")
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()


#株価依存性を見る(ボラティリティも変える)
#権利行使価格,リスクフリーレート,配当利回り,期間,初期時間,ボラティリティ
def stock():
    x = np.empty(0)
    y1 = np.empty(0)
    y2 = np.empty(0)
    y3 = np.empty(0)
    y4 = np.empty(0)
    y5 = np.empty(0)
    y6 = np.empty(0)
    y7 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(0,150):
        sig=0.01
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        x= np.append(x, S)
        y1= np.append(y1, call)

    for i in range(0,150):
        sig=0.05
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y2= np.append(y2, call)

    for i in range(0,150):
        sig=0.1
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y3= np.append(y3, call)

    for i in range(0,150):
        sig=0.2
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y4= np.append(y4, call)

    for i in range(0,150):
        sig=0.3
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y5= np.append(y5, call)

    for i in range(0,150):
        sig=0.4
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y6= np.append(y6, call)

    for i in range(0,150):
        sig=0.5
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y7= np.append(y7, call)
    return x,y1,y2,y3,y4,y5,y6,y7


def plot_stock(x,y1,y2,y3,y4,y5,y6,y7):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("call(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend))
    plt.plot(x, y1, label="vol=0.01")
    plt.plot(x, y2, label="vol=0.05")
    plt.plot(x, y3, label="vol=0.1")
    plt.plot(x, y4, label="vol=0.2")
    plt.plot(x, y5, label="vol=0.3")
    plt.plot(x, y6, label="vol=0.4")
    plt.plot(x, y7, label="vol=0.5")
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()



#株価依存性を見る(ボラティリティも変える)
#権利行使価格,リスクフリーレート,配当利回り,期間,初期時間
def vol():
    x = np.empty(0)
    y1 = np.empty(0)
    y2 = np.empty(0)
    y3 = np.empty(0)
    y4 = np.empty(0)
    y5 = np.empty(0)
    y6 = np.empty(0)
    y7 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,101):
        S=85
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        x= np.append(x, sig)
        y1= np.append(y1, call)

    for i in range(1,101):
        S=90
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y2= np.append(y2, call)

    for i in range(1,101):
        S=95
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y3= np.append(y3, call)

    for i in range(1,101):
        S=100
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y4= np.append(y4, call)

    for i in range(1,101):
        S=105
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y5= np.append(y5, call)

    for i in range(1,101):
        S=110
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y6= np.append(y6, call)

    for i in range(1,101):
        S=115
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        y7= np.append(y7, call)

    return x,y1,y2,y3,y4,y5,y6,y7

def plot_vol(x,y1,y2,y3,y4,y5,y6,y7):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("volatility")
    ax.set_ylabel("call(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend))
    plt.plot(x, y1, label="S=85")
    plt.plot(x, y2, label="S=90")
    plt.plot(x, y3, label="S=95")
    plt.plot(x, y4, label="S=100")
    plt.plot(x, y5, label="S=105")
    plt.plot(x, y6, label="S=110")
    plt.plot(x, y7, label="S=115")
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()




#時間依存性を見る(株価Sも変える)
#権利行使価格,リスクフリーレート,配当利回り,初期時間,ボラティリティ
def strike():
    x = np.empty(0)
    y1 = np.empty(0)
    y2 = np.empty(0)
    y3 = np.empty(0)
    y4 = np.empty(0)
    y5 = np.empty(0)
    y6 = np.empty(0)
    y7 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,101):
        S=100
        K=i+50
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
        x= np.append(x, K)
        y1= np.append(y1, call)
    return x,y1

def plot_strike(x,y1):
    K,r,q,tend,t,sig=default()
    S=100
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("strike(yen)")
    ax.set_ylabel("call(yen)")
    ax.set_title('r=' + str(r) + ', S=' + str(S) + ',sigma=' + str(sig) + ',q=' + str(q) + ',T=' + str(tend))
    #ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))

    plt.plot(x, y1)
    plt.legend()
    #plt.plot(x2, y2, color = 'blue', marker = 'v')
    plt.savefig("a.jpg")
    plt.show()

x,y1=strike()
plot_strike(x,y1)
