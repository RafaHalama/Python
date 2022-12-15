import matplotlib.pyplot as plt
import math
import cmath as cm
from scipy.io import wavfile
from scipy.io.wavfile import write
import numpy


class DTFT:
    def __init__(self, signal, f, fs):
        self.signal = signal
        self.f = f
        self.fs = fs
        
    
        
    def dtft(self):
        j=cm.sqrt(-1)
        omega = 2* math.pi * self.f
        ts = 1/self.fs
        
        sum = 0
        for n, fn in enumerate(self.signal):
            sum+= fn *  numpy.exp( -1*j * omega * ts * n)
            
        return sum
    


def RectangleWindow(signal):
        return signal
        
    
def HanningWindow(signal):
        
        N =len(signal) 
        result_signal=[]
        
        for n, val in enumerate (signal):
            result_signal.append(val * (0.5 - 0.5 * cm.cos( 2* math.pi * (n/N))))
            
        return result_signal

def HammingWindow(signal):
        
        N =len(signal) 
        result_signal=[]
        
        for n, val in enumerate (signal):
            result_signal.append(val * (0.54 - 0.46 * cm.cos( 2* math.pi * (n/N))))
            
        return result_signal


def BlackManWindow(signal):
        
        N =len(signal) 
        result_signal=[]
        
        for n, val in enumerate (signal):
            result_signal.append(val * ((0.42 - 0.5 * cm.cos( (2* math.pi * n)/N))+ 0.08 *((4*math.pi * n)/N)))
            
        return result_signal


def TriangleWindow(signal):
      
        N =len(signal)
        result_signal=[]
        
        for n, val in enumerate (signal):
            
            if(n<= N/2):
                result_signal.append(val * (n/(N/2)))
            else:
                result_signal.append(val * (2- (n/(N/2))))
            
        return result_signal



def ChooseWindow(window,signal):
    if(window=="Hanning"):
        return HanningWindow(signal)
    else if(window=="Triangle"):
        return TriangleWindow(signal)
    else if(window=="Hamming"):
        return HammingWindow(signal)
    else if(window=="Rectangle"):
        return RectangleWindow(signal)
        
def main():

    samplerate, signal = wavfile.read('Struna 1 - E.wav') 
    min_frequency =300
    max_frequency = 400
    step = 1

    liczba_probek = int(1/(1/samplerate))

    #mnozenie sygnalu przez okno    
    signal_window = ChooseWindow("Rectangle", signal)
    
    #obciecie sygnalu do sekundy
    subArray = signal_window[0:liczba_probek]
   
    x=[]
    y=[]
    #obliczenie transformaty i widma
    for frequency in numpy.arange(min_frequency, max_frequency, step):
        dtft = DTFT(subArray,frequency, samplerate)
        dtft_wynik = dtft.dtft()
        x.append(frequency)
        wynik = (abs(dtft_wynik))/len(subArray)
        #konwersja widma na decybele
        y.append(20*math.log10(wynik/32767))

    #narysowanie
    
    plt.plot(x, y)
    plt.show()

    
if __name__ == '__main__':
    main()