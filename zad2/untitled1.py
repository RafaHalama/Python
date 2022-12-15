
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
    
    


coefficients_A_1 = [1, 2, 3, 1, 1, 1]
coefficients_B_1 = [0.9, 0.4, 0.2, 0.1]

coefficients_A_2 = [1, 0, 1, 0, 1]
coefficients_B_2 = [0.9, 0.4, 0.2, 0.1]

coefficients_A_3 = [1, 0.5, 0.25, 0.125]
coefficients_B_3 = [0.125, 0.25, 0.5, 1, 2, 3]

sygnal_we_Dirac = [0,0,0,1,0,0,0,0,0,0,0,0,0,0]
sygnal_we_Jednostkowy = [0,0,0,0,1,1,1,1,1,1,1,1]
sygnal_we_naprzemienny = [1,1,1,1,1,-1,-1,-1,-1,-1,0,0,0,0]


filtrIIR1 = systemIIR(coefficients_A_1,coefficients_B_1)
filtrIIR2 = systemIIR(coefficients_A_2,coefficients_B_2)
filtrIIR3 = systemIIR(coefficients_A_3,coefficients_B_3)


print("*******DIRAC*******")
print([filtrIIR1.Wylicz(s) for s in sygnal_we_Dirac])
print([filtrIIR2.Wylicz(s) for s in sygnal_we_Dirac])
print([filtrIIR3.Wylicz(s) for s in sygnal_we_Dirac])
print()

filtrIIR1 = systemIIR(coefficients_A_1,coefficients_B_1)
filtrIIR2 = systemIIR(coefficients_A_2,coefficients_B_2)
filtrIIR3 = systemIIR(coefficients_A_3,coefficients_B_3)



print("*******SKOKOWY*******")
print([filtrIIR1.Wylicz(s) for s in sygnal_we_Jednostkowy])
print([filtrIIR2.Wylicz(s) for s in sygnal_we_Jednostkowy])
print([filtrIIR3.Wylicz(s) for s in sygnal_we_Jednostkowy])
print()

filtrIIR1 = systemIIR(coefficients_A_1,coefficients_B_1)
filtrIIR2 = systemIIR(coefficients_A_2,coefficients_B_2)
filtrIIR3 = systemIIR(coefficients_A_3,coefficients_B_3)


print("********NAPRZEMIENNY********")
print([filtrIIR1.Wylicz(s) for s in sygnal_we_naprzemienny])
print([filtrIIR2.Wylicz(s) for s in sygnal_we_naprzemienny])
print([filtrIIR3.Wylicz(s) for s in sygnal_we_naprzemienny])

