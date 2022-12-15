import matplotlib.pyplot as plt
import math
import cmath as cm
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy as np


def db(x):
    p=sum([val**2 for val in x])/len(x)
    return 10*math.log10(p)



def thd(data):
    sum=0.0
    for r in range( len(data)):
       sum += (data[r])**2

    
    thd = 100*sum**0.5

    return thd

def main():

    f0=1000
    fs = 48000
    step = 1/fs
    N = 0.01 * 48000
    bit=8
  
    delta = 2 * math.pi/N;
    signal =[]
    x =[]
    for i in range(0,int(N)):
            signal.append(math.sin(delta * i))
            x.append(i)


  

    signal_db = db(signal)
    print("poziom sygnalu:")
    print(signal_db)
   
  
    
    w = 1/(2**(bit-1))
    kwant =[]
    
    for value in signal:
        if value!=0: 
            znak = value/abs(value)
        else: 
            znak=0
        kwant.append(((int)(value * (2** (bit-1)))+znak)*w)
  
    widmo = np.fft.fft(kwant)
    print("poziom sygnalu po kwantyzacji:")
    print(db(kwant))
    
   
    
    roznica = abs(db(signal) - db(kwant))
    print("roznica w decybelach:")
    print(roznica)
    sum=0
    indexes =[]

    for hz in range(10,230,10):
     indexes.append(abs(widmo[hz]))
   
  
    print("Total Harmonic Distortion(in percent):")
    print(thd(indexes))
   
    fig, (ax1, ax2,ax3) = plt.subplots(3)
    fig.suptitle('plots')
    ax1.plot(x,signal, label='sin')
    ax1.legend()
    ax2.plot(x, kwant, label ='quantized sin')
    ax3.plot(x,abs(widmo), label='widmo')
    ax2.legend()
    ax3.legend()
    plt.show()

    
if __name__ == '__main__':
    main()