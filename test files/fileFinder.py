import os
import types
from sys import cv2 #verantwoordelijk voor het laden en tonen van img's
import numpy as np

inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
        
if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
    
    currentDirectoryOfImg = os.getcwd() + "\\fase 3 development\steganografie\\test files\\img\\" + inputImgName
    
    
    #checked of het opgegeven absolute route en bestands naam uit komen bij een bestaand bestand
    if os.path.isfile(currentDirectoryOfImg): #os.path.isfile: is een functie die een bool terug geeft; (currentDirectoryOfImg): is de variable met het absolute pad + bestandsnaam
        
        print("image file found") #file found
        cv2.imshow()
    
    else:
        print("not found") #file not found
        print(currentDirectoryOfImg) # debug regel voor tijdens het developen
        noExtentionProvided = True
            
    dirToImgFile = print(os.path.abspath(currentDirectoryOfImg))
    noExtentionProvided = False # noExtentionProvided wordt op false gezet zodat de loop stopt met checken.

    print(dirToImgFile) # bestand locatie van de gevraagde img
    
else:
    print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
