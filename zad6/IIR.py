import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.io import wavfile

class systemIIR:
    
    def __init__(self,coefficients_A, coefficients_B):
        self.coefficients_A = coefficients_A
        self.dane_A = [0] * len(coefficients_A)
        self.coefficients_B = coefficients_B
        self.dane_B = [0] * (len(coefficients_B))
    
    
    def MnozISumujA(self):
        
        suma = 0
        
        for i in range(len(self.coefficients_A)):
            a = self.coefficients_A[i]
            x = self.dane_A[i]
            suma += (a * x)
        
        return suma
    
    def MnozISumujB(self):
        
        suma=0
        for i in range(len(self.coefficients_B)):
            b = self.coefficients_B[i]
            y = self.dane_B[i]
            suma += (b * y)
        return suma
    
    def WpiszNowaA(self,x):
        self.dane_A = [x] + self.dane_A[:-1]
    
    def WpiszNowaB(self,y):
        self.dane_B = [y] + self.dane_B[:-1]

    
    def Wylicz(self,x):
        
        self.WpiszNowaA(x)
        wynik = self.MnozISumujA()
        wynik += self.MnozISumujB()
        self.WpiszNowaB(wynik)
        
        return wynik

def Butterworth(s,s_0,n):
    wynik = 1/(math.sqrt(1+math.pow((s/s_0),2*n)))
    return wynik


        
    return dataT

def find_coeficients_butterworth(fs,fc,N):
    assert(fs/2 >= fc)
    k = np.arange(1,N+1)
    theta = (2*k-1) * np.pi / (2*N)
    pa = -np.sin(theta) + 1j * np.cos(theta)
    
    Fc = fs/np.pi * np.tan(np.pi*fc/fs)
    pa *=2*np.pi*Fc
    
    p=np.divide((1 + pa /(2*fs)), (1- pa/ (2*fs)))
    q = -np.ones(N)
    a= np.real(np.poly(p))
    b = np.poly(q)
    K = sum(a)/sum(b)
    b*=K
    return b,a

def main():
   fs_signal, signal = wavfile.read("Struna 1 - E.wav")
   sygnal = signal[:fs_signal]
   fs = 48000
   fg=10000
   n=2048
 
   
  
   
 
   
   print(find_coeficients_butterworth(fs, fg, 5))
   a = find_coeficients_butterworth(fs, fg, 5)[0]  
   b = find_coeficients_butterworth(fs, fg, 5)[1]
   
   
   filtrIIR = systemIIR(a,b)
   
   data=[]
   for i in range(len(sygnal)):
    y = filtrIIR.Wylicz(sygnal[i])
    data.append(y)
    
   transform_data = abs(np.fft.fft(data))
    
   fig, (ax1, ax2,ax3) = plt.subplots(3)
   fig.suptitle('plots')
   ax1.plot(list(range(fs)), sygnal)
   ax2.plot(list(range(fs)), data)
   ax3.plot(list(range(fs)), transform_data)

   plt.show()

 
    

if __name__ == '__main__':
    main()