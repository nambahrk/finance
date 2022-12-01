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
    K,r,q,tend,t,sig=default()

    for i in range(1,100):
        S=100
        tend=i/100 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, tend)
        y1= np.append(y1, call)

    return x,y1

def plot_time(x,y1):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("time(yr)")
    ax.set_ylabel("put(yen)")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',q=' + str(q))
    #ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))

    plt.plot(x, y1, label="S=100")
    plt.legend()
    #plt.plot(x2, y2, color = 'blue', marker = 'v')
    plt.savefig("a.jpg")
    plt.show()


#risk依存性を見る(株価も変える)
#権利行使価格,配当利回り,期間,初期時間,ボラティリティ
def risk():
    x = np.empty(0)
    y1 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,100):
        S=100
        r=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, r)
        y1= np.append(y1, call)

    return x,y1

def plot_risk(x,y1):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("risk free rate")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',q=' + str(q) + ',T=' + str(tend) + ',sigma=' + str(sig) )
    plt.plot(x, y1, label="S=100")
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()


#株価依存性を見る(ボラティリティも変える)
#権利行使価格,リスクフリーレート,配当利回り,期間,初期時間,ボラティリティ
def stock():
    x = np.empty(0)
    y1 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(0,150):
        S=i+50 #株価
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, S)
        y1= np.append(y1, call)

    return x,y1


def plot_stock(x,y1):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend))
    plt.plot(x, y1)
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()



#株価依存性を見る(ボラティリティも変える)
#権利行使価格,リスクフリーレート,配当利回り,期間,初期時間
def vol():
    x = np.empty(0)
    y1 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,101):
        S=100
        sig=i/200 #時間
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, sig)
        y1= np.append(y1, call)

    return x,y1

def plot_vol(x,y1):
    K,r,q,tend,t,sig=default()
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("volatility")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend))
    plt.plot(x, y1)
    plt.legend()
    plt.savefig("a.jpg")
    plt.show()


#時間依存性を見る(株価Sも変える)
#権利行使価格,リスクフリーレート,配当利回り,初期時間,ボラティリティ
def strike():
    x = np.empty(0)
    y1 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,101):
        S=100
        K=i+50
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, K)
        y1= np.append(y1, call)
    return x,y1

def plot_strike(x,y1):
    K,r,q,tend,t,sig=default()
    S=100
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("strike(yen)")
    ax.set_ylabel("put(yen)")
    ax.set_title('r=' + str(r) + ', S=' + str(S) + ',sigma=' + str(sig) + ',q=' + str(q) + ',T=' + str(tend))
    #ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))

    plt.plot(x, y1)
    plt.legend()
    #plt.plot(x2, y2, color = 'blue', marker = 'v')
    plt.savefig("a.jpg")
    plt.show()


#時間依存性を見る(株価Sも変える)
#権利行使価格,リスクフリーレート,配当利回り,初期時間,ボラティリティ
def dividend():
    x = np.empty(0)
    y1 = np.empty(0)
    K,r,q,tend,t,sig=default()

    for i in range(1,101):
        S=100
        q=i/1000
        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))

        call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
        x= np.append(x, q)
        y1= np.append(y1, call)
    return x,y1

def plot_dividend(x,y1):
    K,r,q,tend,t,sig=default()
    S=100
    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("dividend(yen)")
    ax.set_ylabel("put(yen)")
    ax.set_title('r=' + str(r) + ', S=K=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))
    #ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',sigma=' + str(sig) + ',T=' + str(tend))

    plt.plot(x, y1)
    plt.legend()
    #plt.plot(x2, y2, color = 'blue', marker = 'v')
    plt.savefig("a.jpg")
    plt.show()

x,y1=strike()
plot_strike(x,y1)
