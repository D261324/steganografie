import os
import sys
import numpy as np
from PIL import Image

def msgToBinairy(msg):
    # voor string
    print(msg)
    if type(msg) == str:
        return ''.join([format(ord(i),"08b")for i in msg])
        #return ''.join(map(bin,bytearray(msg,encoding='utf-8')))
    # voor 
    elif type(msg) == bytes or type(msg) == np.ndarray:
        return [format(i ,"08b") for i in msg]
    
    elif type(msg) == int or type(msg) == np.uint8:
        return format(msg, "08b")
    else:
        return TypeError(" invoer type wordt niet ondersteund")
    
#====================================================================================
def loadImg():
    while noExtentionProvided:
        noExtentionProvided = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd

        inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
        findImgFile = False # zorgt er voor dat de loop blijft lopen tot dat de variable op true wordt gezet
        
        dirFilePath = os.path.exists("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
        if dirFilePath == True:
            print("gevonden!")
            if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
                noExtentionProvided = False
                img = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName) 
                img.show() 
                return inputImgName, img
            else:
                print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
                
        else:
            print("niet gevonden!")
            

        # img search start
inputImgName, img = loadImg()
    
x = 0 
y = 0     



#locatie van de img in kwestie
rgbValueImage = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName, "r")
posPixelValue = list(img.getpixel((x,y)))# haalt info uit de img op. dit word in een object gezet

r,g,b = posPixelValue[0], posPixelValue[1], posPixelValue[2] #rbg waardes opslaan in makkelijker te hendele code

#vrij splitsen en om zetten van de binaire code van de r/g/b waardes
binR = msgToBinairy(r) #rood    255
binG = msgToBinairy(g) #groen   255
binB = msgToBinairy(b) #blauw   255


# hier maak een nieuwe lijst aan om de binaire code in te kunnen opslaan
rgbPerPixelList = list()

for pos in range(r,g,b):
    rgbPerPixelList += r,g,b
    

# berekening benodigde bits + print van binairy voor lengte waarde
count = 0
for value in rgbPerPixelList: # loop om iedere rgb value's 8-bits +1 te representeren voor count 
    lengthLen = int(value)
    count += 1 # total value

print("======================")
print(f"{rgbPerPixelList}\n dit zijn 3 pixels pik; 24 / 8")
print("======================")
print(f"{count}\ndit is de count voor aantal benodigde bits ;)")
print("======================")


# gebruik print(5 % 2) / print(5 % 2) om te bepalen of er een 1(odd) of 0(even) rgb waarde moet komen
    # pix = list(rgbPerPixelList)
    # print(pix)


# print(binPerBin)
# x = 0 #count
# binPerBin = list(binR) #lege dict voor de binaire waardes van de rgb
# binPerBin += list(binB)
#een bitwiseor

#print(len(binPerBin))




    





        
        
        
#rgb_pixel_value = img.getpixel()
# sequence_of_pixels = rgbValueImage.getdata() # haalt info uit de img op. dit word in een object gezet
# list_of_pixels = sequence_of_pixels # hier word de data in een lijst gezet
# sizeInBytes = print(list_of_pixels)
# print(sizeInBytes)
#idee!!!
# 1. zet ieder item uit de rgb reek om naar binaire code(dit kan als het goed is met de bin() functie) 
#my_pixelList = 



# 2. deze waardes split je op in bytes()
    #2.2 probeer ook om deze waardes los in een list op te slaan

    
# 3. som om lengte payload te bepalen
#   3.1 payload length in binairy (img1.jpg; hello, length
#   3.2 13) * 8 = 104 + binairy waarde van int 13(~120 
#   bits).
#   3.3 payloadLentgh + (81*3*8=1944 bits) = 
#   1840 bits totaal over
#   3.4for x in range (120)    
        #voorbeeld: z = (1,2,3,4,5)
        # x = z[counterStartValue(0):counterEndValue(5)]
#   3.5 list.append(counter) = +1 / -1 om de binair 
#   op te slaan in de string van de geconverteerde img
#   3.6 print(newStegoList)
#   3.7 print(len(newStegoList))
#   3.8 converteer binair terug naar 
#   rgb ([255,255,255])
#   3.8 sla rgb op en voeg aan elkaar toe
#   3.9 copy save het nieuwe stego bestand naar een 
#   specifieke map daar voor

#4. toon de nieuw verwerkte stego img in de console of 
#   extern

#5. end de loop 
#6. return naar main menu 
            
# print(len(list_of_pixels))
# print(len(sequence_of_pixels))
    