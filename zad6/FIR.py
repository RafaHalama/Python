import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile


class systemFIR:
    
    def __init__(self,wspolczynniki):
        self.wspolczynniki = wspolczynniki
        self.dane = []
        
        for i in range(len(wspolczynniki)):
            self.dane.append(0)
    
    
    def MnozISumuj(self):
        
        suma = 0
        
        for i in range(len(self.wspolczynniki)):
            a = self.wspolczynniki[i]
            x = self.dane[i]
            suma += (a * x)
        
        return suma
    
    def WpiszNowa(self,x):
        
        indeks = len(self.wspolczynniki) - 1
        
        for i in range(len(self.wspolczynniki)):
            if(i < len(self.wspolczynniki)):
                self.dane[indeks] = self.dane[indeks - 1]
                indeks -= 1
                
        self.dane[0] = x
    
    
    def Wylicz(self,x):
        
        self.WpiszNowa(x)
        wynik = self.MnozISumuj()
        
        return wynik
    

def Butterworth(s,s_0,n):
    wynik = 1/(math.sqrt(1+math.pow((s/s_0),2*n)))
    return wynik

def okno_trojkatne(data):
    dataT = []
    N = len(data)
    for i in range(0,N//2):
        dataT.append(data[i] * ((2*i - 1)/N))
    for i in range(N//2, N):
        dataT.append(data[i] * (2 - ((2*i - 1)/N)))
       
        
    return dataT



def main():
   fs_signal, signal = wavfile.read("Struna 1 - E.wav")
   sygnal = signal[:fs_signal]
   fs = 48000
   fg=10000
   n=204
  
   
   x = []
   data = []
   
   for hz in np.arange(0, fs/2, step=fs/n):
       x.append(hz)
       data.append(Butterworth(hz,fg,5))
    
    
   for hz in np.arange(fs/2, fs, step=fs/n):
        x.append(hz)
        
   
   data += data[::-1]
   
   
   wspolczynniki = np.fft.ifft(data)
   trojkatne = okno_trojkatne(wspolczynniki)
   
   filtrFIR = systemFIR(trojkatne)
   
   filtered=[]
   for i in range(len(sygnal)):
    y = filtrFIR.Wylicz(sygnal[i])
    filtered.append(y)
    
   
  
   transform = abs(np.fft.fft(filtered))
    
   fig, (ax1, ax2,ax3,ax4,ax5,ax6) = plt.subplots(6)
   fig.suptitle('plots')
   ax1.plot(x, data)
   ax2.plot(x,wspolczynniki)
   ax3.plot(x, trojkatne)
   ax4.plot(range(fs), sygnal)
   ax5.plot(range(fs), filtered)
   ax6.plot(range(fs), transform)
 
  #program wykonuje sie okolo 30 sekund
   plt.show()

    

if __name__ == '__main__':
    main()