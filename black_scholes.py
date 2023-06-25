import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import norm

#parameter
def default():
    stock_price=100   
    strike=100   
    r=0.03  #rate
    q=0.01  #dividend
    t_maturity=1  
    t=0      
    volatility=0.2

    return stock_price,strike,r,q,t_maturity,t,volatility


def time(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(70,130,7) #Stock price
    
    grid=100 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=list[i]
            t_maturity = j/grid #maturity
            d1 = (math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2 = (math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            callput_tmp = sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)
            callput  = np.append(callput,callput_tmp)  #call or put price each stock price
        y= np.append(y, np.array([callput]),axis=0)  #y axis (call or put price)

    for j in range(1,1+grid):
        x= np.append(x, j/grid) #x axis (maturity)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("time(yr)")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"(yen)")
    ax.set_title(str(name) + 'option, r=' + str(r) + ', strike=' + str(strike) + ',sigma=' + str(volatility) + ',q=' + str(q))


    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="stock_price="+ str(list[i]))
    plt.legend()
    plt.savefig("time_"+name+".png")
    plt.clf()


def risk(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(70,130,7) #Stock price
    
    grid=100 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=list[i]
            r=j/1000  #rate
            d1 = (math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2 = (math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            callput_tmp = sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)
            callput  = np.append(callput,callput_tmp)  #call or put price each stock price
        y= np.append(y, np.array([callput]),axis=0)  #y axis (call or put price)

    for j in range(1,1+grid):
        x= np.append(x, j/1000)   #x axis (rate)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("risk free rate")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"(yen)")
    ax.set_title(str(name) + 'option, strike=' + str(strike) + ',q=' + str(q) + ',T=' + str(t_maturity) + ',sigma=' + str(volatility) )
        
    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="stock_price="+ str(list[i]))
    plt.legend()
    plt.savefig("risk_"+name+".png")
    plt.clf()


def stock(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(0.1,1,10) #Stock price
    
    grid=150 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 


    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=j+50
            t_maturity=list[i]
            d1 = (math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2 = (math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            callput_tmp = sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)
            callput  = np.append(callput,callput_tmp)  #call or put price each stock price
        y= np.append(y, np.array([callput]),axis=0)  #y axis (call or put price)

    for j in range(1,1+grid):
        x= np.append(x, j+50)    #x axis (Stock Price)


    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"(yen)")
    ax.set_title(str(name) + 'option, strike=' + str(strike) + ',r=' + str(r) + ',q=' + str(q) +',sigma=' + str(volatility))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(round(list[i],1)))
    plt.legend()
    plt.savefig("stock_"+name+".png")
    plt.clf()





def vol(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(70,130,7) #Stock price
    
    grid=100 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=list[i]
            volatility=j/200
            d1 = (math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2 = (math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            callput_tmp = sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)
            callput  = np.append(callput,callput_tmp)  #call or put price each stock price
        y= np.append(y, np.array([callput]),axis=0)  #y axis (call or put price)

        
    for j in range(1,1+grid):
        x= np.append(x, j/200)    #x axis (volatility)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("volatility")
    
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"(yen)")
    ax.set_title(str(name) + 'option, strike=' + str(strike) + ',r=' + str(r) + ',q=' + str(q) +',T=' + str(t_maturity))


    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="stock_price="+ str(list[i]))
    plt.legend()
    plt.savefig("volatility_"+name+".png")
    plt.clf()



def strike(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(70,130,7) #Stock price
    
    grid=100 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=list[i]
            strike=j+50
            d1 = (math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2 = (math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            callput_tmp = sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)
            callput  = np.append(callput,callput_tmp)  #call or put price each stock price
        y= np.append(y, np.array([callput]),axis=0)  #y axis (call or put price)

        
    for j in range(1,1+grid):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("strike(yen)")

    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"(yen)")
    ax.set_title(str(name) + 'option, r=' + str(r) + ', stock_price=' + str(stock_price) + ',sigma=' + str(volatility) + ',q=' + str(q) + ',T=' + str(t_maturity))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="stock_price="+ str(list[i]))
    plt.legend()
    plt.savefig("strike_"+name+".png")
    plt.clf()



def calling(sign,stock_price,strike,r,q,t_maturity,t,volatility,d1,d2):
    return sign*stock_price*math.exp(q*t-q*t_maturity)*norm.cdf(x=sign*d1, loc=0, scale=1)-sign*strike*math.exp(r*t-r*t_maturity)*norm.cdf(x=sign*d2, loc=0, scale=1)


def delta(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()
    list=np.linspace(0.1,1,10)
    
    grid=150 #split

    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=j+50
            t_maturity=list[i]
            h = 0.001
            d1=(math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2=(math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))

            call = (calling(sign,stock_price+h,strike,r,q,t_maturity,t,volatility,d1,d2)-calling(sign,stock_price-h,strike,r,q,t_maturity,t,volatility,d1,d2))/2*h
            callput= np.append(callput,call) 

        y= np.append(y, np.array([callput]),axis=0)

    for j in range(1,1+grid):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"delta")
    ax.set_title(str(name) + 'option, r=' + str(r) + ', strike=' + str(strike) + ',sigma=' + str(volatility) + ',q=' + str(q) + ',T=' + str(t_maturity))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(round(list[i],1)))
    plt.legend()
    plt.savefig("delta_"+name+".png")
    plt.clf()



def gamma(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()
    list=np.linspace(0.1,1,10)
    
    grid=150 #split
    
    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=j+50
            t_maturity=list[i]
            h = 0.0001
            d1=(math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2=(math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))

            #callput_tmp = (calling(stock_price+2*h)+calling(stock_price-2*h)-2*calling(stock_price))/4*h*h
            #callput= np.append(callput,callput_tmp) 

            call_tmp = (calling(sign,stock_price+2*h,strike,r,q,t_maturity,t,volatility,d1,d2)+calling(sign,stock_price-2*h,strike,r,q,t_maturity,t,volatility,d1,d2)-2*calling(sign,stock_price,strike,r,q,t_maturity,t,volatility,d1,d2))/2*h
            callput= np.append(callput,call_tmp) 

        y= np.append(y, np.array([callput]),axis=0)

    for j in range(1,1+grid):
        x= np.append(x, j+50)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"gamma")
    ax.set_title(str(name) + 'option, r=' + str(r) + ', strike=' + str(strike) + ',sigma=' + str(volatility) + ',q=' + str(q) + ',T=' + str(t_maturity))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(round(list[i],1)))
    plt.legend()
    plt.savefig("gamma_"+name+".png")
    plt.clf()


def vega(sign=1): #sign=1(call),sign=-1(put)
    stock_price,strike,r,q,t_maturity,t,volatility=default()

    list = np.linspace(70,130,7) #Stock price
    
    grid=100 #split

    x = np.empty(0)
    y = np.empty((0,grid)) 

    for i in range(0,len(list)):
        callput=np.empty(0)
        for j in range(1,1+grid):
            stock_price=list[i]
            volatility=j/200
            h = 0.00001
            d1=(math.log(stock_price/strike)+(r-q+volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))
            d2=(math.log(stock_price/strike)+(r-q-volatility*volatility/2)*(t_maturity-t))/(volatility*math.sqrt(t_maturity-t))

            callput_tmp = (calling(sign,stock_price+h,strike,r,q,t_maturity,t,volatility,d1,d2)-calling(sign,stock_price-h,strike,r,q,t_maturity,t,volatility,d1,d2))/2*h
            callput= np.append(callput,callput_tmp) 

        y= np.append(y, np.array([callput]),axis=0)

    for j in range(1,1+grid):
        x= np.append(x, j/200)

    fig = plt.figure(figsize=(10, 5))
    ax=fig.subplots()
    ax.set_xlabel("stock price(yen)")
    if sign == 1:
        name = "call"
    if sign == -1:
        name = "put"    
    ax.set_ylabel(str(name)+"vega")
    ax.set_title(str(name) + 'option, r=' + str(r) + ', strike=' + str(strike) + ',stock_price=' + str(stock_price) + ',q=' + str(q) + ',T=' + str(t_maturity))

    for i in range(0,len(list)):   
        z=y[i]   
        plt.plot(x, z, label="T="+ str(round(list[i],1)))
    plt.legend()
    plt.savefig("vega_"+name+".png")
    plt.clf()

"""
time(1)
time(-1)
risk(1)
risk(-1)
stock(1)
stock(-1)
vol(1)
vol(-1)
strike(1)
strike(-1)
"""

delta(1)
delta(-1)
gamma(1)
gamma(-1)
vega(1)
vega(-1)
