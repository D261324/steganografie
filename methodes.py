import os
import types
from pkgutil import ImpImporter
from re import I
from PIL import Image
import numpy as np

def modPix(pix, data):
 

    datalist = msgToBinairy(data)

    lendata = len(datalist)

    imdata = iter(pix)
 

    for i in range(lendata):
 

        # Extracting 3 pixels at a time

        pix = [value for value in imdata.__next__()[:3] +

                                imdata.__next__()[:3] +

                                imdata.__next__()[:3]]
 

        # Pixel value should be made

        # odd for 1 and even for 0

        for j in range(0, 8):

            if (datalist[i][j] == '0' and pix[j]% 2 != 0):

                pix[j] -= 1
 

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):

                if(pix[j] != 0):

                    pix[j] -= 1

                else:

                    pix[j] += 1

                # pix[j] -= 1
 

        # Eighth pixel of every set tells

        # whether to stop ot read further.

        # 0 means keep reading; 1 means thec

        # message is over.

        if (i == lendata - 1):

            if (pix[-1] % 2 == 0):

                if(pix[-1] != 0):

                    pix[-1] -= 1

                else:

                    pix[-1] += 1
 

        else:

            if (pix[-1] % 2 != 0):

                pix[-1] -= 1
 

        pix = tuple(pix)

        yield pix[0:3]

        yield pix[3:6]

        yield pix[6:9]


def encoding ():
    print("we starten het proces van encoderen...") 
    
    noExtentionProvided = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd
    
    while noExtentionProvided:
        # img search start
            inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
            
            dirFilePath = os.path.exists("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
            if dirFilePath == True:
                print("gevonden!")
                if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
                    noExtentionProvided = False
                    img = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName) 
                    img.show() 
                else:
                    print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
                    
            else:
                print("niet gevonden!")
           
    # img search end
    else:  
        lenghtImg = len(inputImgName)
        inputImgNameInBin = list(msgToBinairy(inputImgName))
        print(lenghtImg)
        
        msg = input("schrijf uw bericht: \n")
        encodedMsg = msgToBinairy(msg)
        
        binListMsg = list(encodedMsg)
        lenghtMsg = len(binListMsg)
        

        print(binListMsg)
        print(len(encodedMsg))
        print(inputImgNameInBin)
        print(len(inputImgNameInBin))
        
        print (inputImgName, lenghtImg, msg, lenghtMsg )
        return(lenghtImg, lenghtMsg, binListMsg)

#optie 2
def decoding():
    imgNameInput = input("Enter image name(with extension) : ")
    img = Image.open("C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + imgNameInput) 
    data = ''
    imgdata = iter(img.getdata())
    
    while (True):
        pixels = [value for value in imgdata.next()[:3] +
                                imgdata.next()[:3] +
                                imgdata.next()[:3]]
        print(pixels)
        print(len(pixels))
        print("+++++++++++++++++++++++++++++++++++++++++++++++")
       
 
    

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

def payloadSom(inputImgNameInBin, binListMsg):
    payloadFile = print(len(inputImgNameInBin))
    payloadMsg = print(len(binListMsg))
    print(payloadFile)
    print(payloadMsg)
    
# ======================== over bodige code =======================
    # msg = "hioi"
# countValue = len(msgToBinairy(msgToBinairy))
    
# print(countValue)
# print(msgToBinairy(binListMsg))
    