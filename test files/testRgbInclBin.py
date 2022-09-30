#imports
import os
import sys
import numpy as np
from PIL import Image

x = 0
y = 0

# test data van een random img
def imgRgbValues(inputImgName):
    img = Image.open("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
    posPixelValue = list(img.getpixel((x,y)))# haalt info uit de img op. dit word in een object gezet
    
    # rgb values ophalen
    r,g,b = posPixelValue[0], posPixelValue[1], posPixelValue[2] #rbg waardes opslaan in makkelijker te hendele code

    #lopen door alle pixels hun rgb waardes
    for pos in range(r,g,b):
        rgbPerPixelList += r,g,b
    #hier onder is het idee dat we zorgen voor de een totale int waarde van de rgb lijst en deze terug sturen 
    
    #+++++++++++++!!!!!!!!!! werkt nog niet !!!!!!!!!!!++++++++++++++++++
    # lengthImgrgbSize_Itar = len(range(r,g,b))
    # lengthImgrgbSize_Itar(lengthImgrgbSize_Itar(r))
    # lengthImgrgbSize_Itar(lengthImgrgbSize_Itar(g))
    # lengthImgrgbSize_Itar(lengthImgrgbSize_Itar(b))

    #return lengthImgrgbSize_Itar
    #+++++++++++++!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!++++++++++++++++++

# hier gaan we vragen wat de file naam wordt; sidenode: het is hier nog niet duidelijk te zien maar dit is voor decoderen ofwel de kopie/ stego img
inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
function = imgRgbValues(inputImgName)
# for x in lengthImgrgbSize_Itar:
#     print(next(x))


