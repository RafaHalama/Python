from PIL import Image
import os
from array import *
#Wczytanie obrazu

file_counter =0

a = []

directory = os.path.dirname(os.path.realpath("script.py"))

for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        im = Image.open(filename) 
        obraz_rgb = im.convert("RGB")
        rozdzielczosc = im.size
     
        if(file_counter ==0):
            img = Image.new("RGB", (rozdzielczosc[0],rozdzielczosc[1]))
            pixels = img.load()
            a = [[0 for x in range(3)] for y in range(rozdzielczosc[0]* rozdzielczosc[1])]
         
          
        for i in range(rozdzielczosc[0]):
            for j in range (rozdzielczosc[1]):
                r,g,b = im.getpixel((i,j))
                r2,g2,b2 = a[rozdzielczosc[1]*i+j]
                a[rozdzielczosc[1]*i+j] = [r+r2, g+g2, b+b2]
                
            
            
         
        file_counter +=1
        
        continue
    else:
        continue




for i in range(rozdzielczosc[0]):
            for j in range (rozdzielczosc[1]):
                r,g,b = a[rozdzielczosc[1]*i+j]
                r = int(r/file_counter)
                g = int(g/file_counter)
                b = int(b/file_counter)
               
                pixels[i,j] = (r,g,b)
                
                

#program wykonuje sie okolo minute
#Pokazanie obrazu
img.show() 
img.save("new.png")
