import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.io import wavfile
samplerate, data = wavfile.read('Struna 1 - E.wav') #Plik mono!!!!!
from scipy.io.wavfile import write

print ("Częstotliwość próbkowania ......... " + str(samplerate) + " Hz")
print ("Liczba próbek ..................... " + str(len(data)))

okres_probkowania = 1 / samplerate

print ("Okres próbkowania ................. " + str(okres_probkowania) + " s")

czas_trwania_nagrania = len(data) * okres_probkowania

print ("Czas trwania nagrania ............. " + str(czas_trwania_nagrania) + " s")


ile_przesunac = float(input("0 ile czasu przsunac sygnal?"))
liczba_probek = int(ile_przesunac/okres_probkowania)
print("Aby przesunac sygnal o czas: " + str(ile_przesunac) + " nalezy wstawic " 
+ str(liczba_probek) )
data_x = range(len(data))



wzmocnienie = 0.1

#stworzenie drugiej tablicy
data2 = np.empty(len(data)+ liczba_probek, dtype=object)

#wypelnienie poczatku zerami
i = 0
while i < liczba_probek:
    data2[i] = 0
    i += 1


#wypelnienie tablicy z delayem sygnalem z pliku

i = liczba_probek
while i < len(data)+ liczba_probek:
    data2[i] = data[i - liczba_probek]
    i += 1


#dodanie wzmocnienia
data2 = np.multiply(data2,wzmocnienie, casting='unsafe')

data2 = np.array(data2, dtype=np.int16)


#dodanie dzwieku na poczatek

i=0
while i < liczba_probek:
    data2[i] = data[i]
    i += 1

data2_x = range(len(data2))

#obliczenie decybeli

c1 = (2**15 - 1)**2

dbs1 = 20*math.log10( math.sqrt(np.mean(data**2) / c1))
dbs2 = 20*math.log10( math.sqrt(np.mean(data2**2) / c1))

print("sygnal przed w decybelach: " + str(dbs1))
print("sygnal po w decybelach: " + str(dbs2))



plt.plot(data2_x, data2)

plt.show()




write("kopia.wav",samplerate,data2)