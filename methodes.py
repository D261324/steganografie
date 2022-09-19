def encoding ():
    print("we starten het proces van encoderen...") 
    
    inputImgName = "blabla"
    noExtentionProvided = True # dit zorgt dat de loop blijft lopen zolang de waarde niet veranderd
    
    while noExtentionProvided:
        
        
        
        inputImgName = input("hoe heet het volledige bestand + extentie die je wil gebruiken: ")
        
        if inputImgName.lower().endswith(('.png', '.jpg', '.jpeg')): # Check filename, if ok:
            noExtentionProvided = False
        else:
            print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
    
    else:  
        lenghtImg = len(inputImgName)
        print(lenghtImg)
        
        msg = input("schrijf uw bericht: \n")
        lenghtMsg = len(msg) * 8
        
        print (inputImgName, lenghtImg, msg, lenghtMsg )
        return(lenghtImg, lenghtMsg)


def decoding():
    inputCheck = False
    
    
    return
    # lengtcaracters = len(inputImgName)
    # print(lengtcaracters)

    