import os
import types
from pkgutil import ImpImporter
from re import I
from PIL import Image 

#import cv2
import numpy as np


def encoding ():
    print("we starten het proces van encoderen...") 
    
    noExtentionProvided = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd
    
    while noExtentionProvided:
        # img search start
            inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
            findImgFile = False # zorgt er voor dat de loop blijft lopen tot dat de variable op true wordt gezet
            
            if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
                noExtentionProvided = False
                dirFilePath = os.path.exists("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
                
                if dirFilePath:
                    print("gevonden!")
                    img = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName) 
                    img.show() 
                else:
                    print("niet gevonden!")
            else:
                print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
    # img search end
    else:  
        lenghtImg = len(inputImgName)
        print(lenghtImg)
        
        msg = input("schrijf uw bericht: \n")
        encodedMsg = msgToBinairy(msg)
        
        print(len(encodedMsg))
        print(encodedMsg)
        #print (inputImgName, lenghtImg, msg, lenghtMsg )
        #return(lenghtImg, lenghtMsg)


def decoding():
    inputCheck = False
    
    # lengtcaracters = len(inputImgName)
    # print(lengtcaracters)
    
#def showImg(imgFile):
    cv2.imshow(imgFile) #werkt nog niet 
    
#def useablePixelSize():
    pixelSize = 24

#def charToAsciiValue(msg):
    unicode_value = [ord(x) for x in msg]
    
    
    
# msgTobinairy start; deze methode zet de caracters om naar binairy 
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
# msgTobinairy end;
# msg = "hioi"
# countValue = len(somMsgToBinairy(msg))
    
# print(countValue)
# print(somMsgToBinairy(msg))
