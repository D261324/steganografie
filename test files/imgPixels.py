from operator import length_hint
import os
import sys
import numpy as np
from PIL import Image

def msgToBinairy(msg):
    # voor string
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
noExtentionProvided = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd

while noExtentionProvided:
    # img search start
        inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
        findImgFile = False # zorgt er voor dat de loop blijft lopen tot dat de variable op true wordt gezet
        
        dirFilePath = os.path.exists("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
        if dirFilePath == True:
            print("gevonden!")
            if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
                noExtentionProvided = False
                img = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName) 
                #img.show() 
            else:
                print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
                
        else:
            print("niet gevonden!")
   
x = 0 
y = 0     



#locatie van de img in kwestie
rgbValueImage = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName, "r")
rgb_pixel_value = img.getpixel((x,y))# haalt info uit de img op. dit word in een object gezet
print(rgb_pixel_value)
r,g,b = rgb_pixel_value[0], rgb_pixel_value[1], rgb_pixel_value[2] #rbg waardes opslaan in makkelijker te hendele code

#vrij splitsen en om zetten van de binaire code van de r/g/b waardes
binR = msgToBinairy(r) #rood    255 
binG = msgToBinairy(g) #groen   255
binB = msgToBinairy(b) #blauw   255


x = 0 #count
binPerBin = [] #lege dict voor de binaire waardes van de rgb
# binPerBin[] wordt hier onder gevult door apart rood groen en blauw toe te voegen
binPerBin.append(int(binR))
binPerBin.append(binG)
binPerBin.append(binB)

print(binPerBin)
binPerBin[0] = binR.split('\n')
for bit in binR:
    EightBits = []
    EightBits.append(bit)
    x += 1
print(len(EightBits))
# for bit in binPerBin[x]:
#     print(bit(0))
    




# sequence_of_pixels = rgbValueImage.getpixel(rgbValueImage,"RGB") 
# list_of_pixels = list(sequence_of_pixels) 
# for x in list_of_pixels: # voor x (aantal) pixels in sequence(reeks) 
#         print(list_of_pixels)
        
        
        
#rgb_pixel_value = img.getpixel()
# sequence_of_pixels = rgbValueImage.getdata() # haalt info uit de img op. dit word in een object gezet
# list_of_pixels = sequence_of_pixels # hier word de data in een lijst gezet
# sizeInBytes = print(sys.getsizeof(list_of_pixels), "bytes", os.sep)
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
    