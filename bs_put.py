import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

#parameter
def default():
    S=100
    K=100
    r=0.03
    q=0.01
    tend=1
    t=0
    sig=0.2

    return S,K,r,q,tend,t,sig

#時間依存性を見る(株価Sも変える)
#権利行使価格,リスクフリーレート,配当利回り,初期時間,ボラティリティ


def time():
    S,K,r,q,tend,t,sig=default()

    list=[90,95,100,105,110,115]
    
    #分割数
    split=100
    
    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=list[i]
            tend = j/split #時間
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            calls=np.append(calls,call) 
        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j/split)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("time(yr)")
    ax.set_ylabel("put(yen)")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',q=' + str(q))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="S="+ str(list[i]))
    plt.legend()
    plt.savefig("time.jpg")
    plt.show()





def risk():
    S,K,r,q,tend,t,sig=default()
    list=[85,90,95,100,105,110,115]
    
    #分割数
    split=100

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=list[i]
            r=j/1000
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            calls=np.append(calls,call) 
        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j/1000)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("risk free rate")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',q=' + str(q) + ',T=' + str(tend) + ',sigma=' + str(sig) )

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="S="+ str(list[i]))
    plt.legend()
    plt.savefig("risk.jpg")
    plt.show()


#株価依存性
def stock():
    S,K,r,q,tend,t,sig=default()
    list=[0.1,0.5,1]
    
    #分割数
    split=150

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=j+50
            tend=list[i]
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            calls= np.append(calls,call) 
        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j+50)


    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',sigma=' + str(sig))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(list[i]))
    plt.legend()
    plt.savefig("stock.jpg")
    plt.show()



def vol():
    S,K,r,q,tend,t,sig=default()
    list=[85,90,95,100,105,110,115]
    
    #分割数
    split=100

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=list[i]
            sig=j/200
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            calls= np.append(calls,call) 
        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j/200)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("volatility")
    ax.set_ylabel("put(yen)")
    ax.set_title('K=' + str(K) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(tend))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="S="+ str(list[i]))
    plt.legend()
    plt.savefig("volatility.jpg")
    plt.show()



def strike():
    S,K,r,q,tend,t,sig=default()
    list=[85,90,95,100,105,110,115]
    
    #分割数
    split=100

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=list[i]
            K=j+50
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            call = -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            calls= np.append(calls,call) 
        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("strike(yen)")
    ax.set_ylabel("put(yen)")
    ax.set_title('r=' + str(r) + ', S=' + str(S) + ',sigma=' + str(sig) + ',q=' + str(q) + ',T=' + str(tend))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="S="+ str(list[i]))
    plt.legend()
    plt.savefig("strike.jpg")
    plt.show()


def delta():
    S,K,r,q,tend,t,sig=default()
    list=[0.1,0.5,1]
    
    #分割数
    split=150

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=j+50
            tend=list[i]
            h = 0.00001
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            def calling(S):
                return -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            
            call = (calling(S+h)-calling(S-h))/2*h
            calls= np.append(calls,call) 

        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("delta")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',q=' + str(q) + ',T=' + str(tend))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(list[i]))
    plt.legend()
    plt.savefig("delta.jpg")
    plt.show()



def gamma():
    S,K,r,q,tend,t,sig=default()
    list=[0.1,0.5,1]
    
    #分割数
    split=150

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=j+50
            tend=list[i]
            h = 0.000001
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            def calling(S):
                return -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            
            call = (calling(S+h)+calling(S-h)-calling(S)-calling(S))/h*h
            calls= np.append(calls,call) 

        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("gamma")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',sigma=' + str(sig) + ',q=' + str(q) + ',T=' + str(tend))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(list[i]))
    plt.legend()
    plt.savefig("gamma.jpg")
    plt.show()



def vega():
    S,K,r,q,tend,t,sig=default()
    list=[85,90,95,100,105,110,115]

    #分割数
    split=100

    #配列初期化
    x = np.empty(0)
    y = np.empty((0,split)) 

    for i in range(0,len(list)):
        calls=np.empty(0)
        for j in range(1,1+split):
            S=list[i]
            sig=j/200
            h = 0.00001
            d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
            def calling(S):
                return -S*math.exp(q*t-q*tend)*norm.cdf(x=-d1, loc=0, scale=1)+K*math.exp(r*t-r*tend)*norm.cdf(x=-d2, loc=0, scale=1)
            
            call = (calling(S+h)-calling(S-h))/2*h
            calls= np.append(calls,call) 

        y= np.append(y, np.array([calls]),axis=0)

    for j in range(1,1+split):
        x= np.append(x, j/200)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    ax.set_ylabel("vega")
    ax.set_title('r=' + str(r) + ', K=' + str(K) + ',S=' + str(S) + ',q=' + str(q) + ',T=' + str(tend))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(list[i]))
    plt.legend()
    plt.savefig("vega.jpg")
    plt.show()




stock()