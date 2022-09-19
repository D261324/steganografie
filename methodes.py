def encoding ():
    print("we starten het proces van encoderen...") 
    inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
        
    if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')):
        
        inputCheck = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd
        while inputCheck == True:
            lenghtImg = len(inputImgName)
            print(lenghtImg)
            
            
            
            msg = input("schrijf uw bericht: \n")
            lenghtMsg = len(msg)
            
            print (lenghtImg, lenghtMsg )
            return(lenghtImg, lenghtMsg)
def decoding():
    inputCheck = False
    print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
    
    return
    # lengtcaracters = len(inputImgName)
    # print(lengtcaracters)

    