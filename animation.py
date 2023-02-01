import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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

def anime_strike():
        S,K,r,q,tend,t,sig=default()
        list=[85,90,95,100,105,110,115]

        #分割数
        split=100

        #配列初期化
        x = np.empty(0)
        y = np.empty((0,split)) 

        ims = []
        fig, ax = plt.subplots()

        for j in range(1,1+split):
                x= np.append(x, j+50)

        for i in range(0,len(list)):
                
                calls=np.empty(0)
                for j in range(1,1+split):
                        S=list[i]
                        K=j+50
                        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
                        calls= np.append(calls,call) 
                y= np.append(y, np.array([calls]),axis=0)

                z=y[i]   
                im = ax.plot(x, z)
                ax.set_xlabel("strike(yen)")
                ax.set_ylabel("call(yen)")
                title = ax.text(0, 1.05, 'S= {}'.format(S) + ',K= {}'.format(K) + ',r= {}'.format(r) + ',sigma= {}'.format(sig)  +',q= {}'.format(q) +',T= {}'.format(tend) ,transform=ax.transAxes, fontsize='large')
                ims.append(im+ [title])                  # グラフを配列 ims に追加
        

        # 10枚のプロットを 100ms ごとに表示
        ani = animation.ArtistAnimation(fig, ims, interval=1000)
        plt.show()
        ani.save('strike.gif')



def anime_vol():
        S,K,r,q,tend,t,sig=default()
        list=[85,90,95,100,105,110,115]

        #分割数
        split=100

        #配列初期化
        x = np.empty(0)
        y = np.empty((0,split)) 

        ims = []
        fig, ax = plt.subplots()

        for j in range(1,1+split):
                x= np.append(x, j/200)

        for i in range(0,len(list)):
                
                calls=np.empty(0)
                for j in range(1,1+split):
                        S=list[i]
                        K=j/200
                        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
                        calls= np.append(calls,call) 
                y= np.append(y, np.array([calls]),axis=0)

                z=y[i]   
                im = ax.plot(x, z)
                ax.set_xlabel("volatility")
                ax.set_ylabel("call(yen)")
                #im, = ax.plot(x, z, label="S="+ str(list[i]))
                title = ax.text(0, 1.05, 'S= {}'.format(S) + ',K= {}'.format(K) + ',r= {}'.format(r) + ',sigma= {}'.format(sig)  +',q= {}'.format(q) +',T= {}'.format(tend) ,transform=ax.transAxes, fontsize='large')
                ims.append(im+ [title])                  # グラフを配列 ims に追加
        

        # 10枚のプロットを 100ms ごとに表示
        ani = animation.ArtistAnimation(fig, ims, interval=1000)
        plt.show()
        ani.save('volatility.gif')




def anime_stock():
        S,K,r,q,tend,t,sig=default()
        list=[0.1,0.5,1]

        #分割数
        split=150

        #配列初期化
        x = np.empty(0)
        y = np.empty((0,split)) 

        ims = []
        fig, ax = plt.subplots()

        for j in range(1,1+split):
                x= np.append(x, j+50)

        for i in range(0,len(list)):
                
                calls=np.empty(0)
                for j in range(1,1+split):
                        S=j+50
                        tend=list[i]
                        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
                        calls= np.append(calls,call) 
                y= np.append(y, np.array([calls]),axis=0)

                z=y[i]   
                im = ax.plot(x, z)
                ax.set_xlabel("stock price(yen)")
                ax.set_ylabel("call(yen)")
                #im, = ax.plot(x, z, label="S="+ str(list[i]))
                title = ax.text(0, 1.05, 'S= {}'.format(S) + ',K= {}'.format(K) + ',r= {}'.format(r) + ',sigma= {}'.format(sig)  +',q= {}'.format(q) +',T= {}'.format(tend) ,transform=ax.transAxes, fontsize='large')
                ims.append(im+ [title])                  # グラフを配列 ims に追加
        

        # 10枚のプロットを 100ms ごとに表示
        ani = animation.ArtistAnimation(fig, ims, interval=1000)
        plt.show()
        ani.save('stock.gif')



def anime_risk():
        S,K,r,q,tend,t,sig=default()
        list=[85,90,95,100,105,110,115]

        #分割数
        split=100

        #配列初期化
        x = np.empty(0)
        y = np.empty((0,split)) 

        ims = []
        fig, ax = plt.subplots()

        for j in range(1,1+split):
                x= np.append(x, j/1000)

        for i in range(0,len(list)):
                
                calls=np.empty(0)
                for j in range(1,1+split):
                        S=list[i]
                        r=j/1000
                        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
                        calls= np.append(calls,call) 
                y= np.append(y, np.array([calls]),axis=0)

                z=y[i]   
                im = ax.plot(x, z)
                ax.set_xlabel("risk free rate")
                ax.set_ylabel("call(yen)")
                #im, = ax.plot(x, z, label="S="+ str(list[i]))
                title = ax.text(0, 1.05, 'S= {}'.format(S) + ',K= {}'.format(K) + ',r= {}'.format(r) + ',sigma= {}'.format(sig)  +',q= {}'.format(q) +',T= {}'.format(tend) ,transform=ax.transAxes, fontsize='large')
                ims.append(im+ [title])                  # グラフを配列 ims に追加
        

        # 10枚のプロットを 100ms ごとに表示
        ani = animation.ArtistAnimation(fig, ims, interval=1000)
        plt.show()
        ani.save('risk.gif')




def anime_time():
        S,K,r,q,tend,t,sig=default()
        list=[85,90,95,100,105,110,115]

        #分割数
        split=100

        #配列初期化
        x = np.empty(0)
        y = np.empty((0,split)) 

        ims = []
        fig, ax = plt.subplots()

        for j in range(1,1+split):
                x= np.append(x, j/split)

        for i in range(0,len(list)):
                
                calls=np.empty(0)
                for j in range(1,1+split):
                        S=list[i]
                        tend = j/split #時間
                        d1=(math.log(S/K)+(r-q+sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        d2=(math.log(S/K)+(r-q-sig*sig/2)*(tend-t))/(sig*math.sqrt(tend-t))
                        call = S*math.exp(q*t-q*tend)*norm.cdf(x=d1, loc=0, scale=1)-K*math.exp(r*t-r*tend)*norm.cdf(x=d2, loc=0, scale=1)
                        calls= np.append(calls,call) 
                y= np.append(y, np.array([calls]),axis=0)

                z=y[i]   
                im = ax.plot(x, z)
                ax.set_xlabel("time(yr)")
                ax.set_ylabel("call(yen)")
                #im, = ax.plot(x, z, label="S="+ str(list[i]))
                title = ax.text(0, 1.05, 'S= {}'.format(S) + ',K= {}'.format(K) + ',r= {}'.format(r) + ',sigma= {}'.format(sig)  +',q= {}'.format(q) +',T= {}'.format(tend) ,transform=ax.transAxes, fontsize='large')
                ims.append(im+ [title])                  # グラフを配列 ims に追加
        

        # 10枚のプロットを 100ms ごとに表示
        ani = animation.ArtistAnimation(fig, ims, interval=1000)
        plt.show()
        ani.save('time.gif')

anime_time()