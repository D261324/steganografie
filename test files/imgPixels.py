import os
from PIL import Image

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
                img.show() 
            else:
                print("dit was geen geldig bestands naam. bekijk het bestand in de verkenner")
                
        else:
            print("niet gevonden!")
   
#x = 0 
#y = 0     
#rgb_pixel_value = img_image_rgb.getpixel((x,y))
#img_image_rgb = rgbValueImage.convert("RGB")

#locatie van de img in kwestie
rgbValueImage = Image.open(r"C:\\Users\\stefa\\OneDrive\\Desktop\\software developer\\td4-ssd-3b 2022-2023\\project_extern\\project 1\\fase 3 development\\steganografie\\img\\" + inputImgName)
sequence_of_pixels = rgbValueImage.getdata() # haalt info uit de img op. dit word in een object gezet
list_of_pixels = list(sequence_of_pixels) # hier word de data in een lijst gezet
for x in list_of_pixels: # voor x (aantal) pixels in sequence(reeks) 
    print(list_of_pixels) # print iedere reeks voor iedere pixel
        
#idee!!!
# 1. zet ieder item uit de rgb reek om naar binaire code(dit kan als het goed is met de bin() functie) 
# 2. deze waardes split je op in bytes()
    #2.2 probeer ook om deze waardes los in een list op te slaan
# 3. som om lengte payload te bepalen
#   3.1 payload length in binairy (img1.jpg; hello, length
#   3.2 13) * 8 = 104 + binairy waarde van int 13(~120 
#   bits).
#   3.3 payloadLentgh + (81*3*8=1944 bits) = 
#   1840 bits totaal over
#   3.4for x in range (120)
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
            
print(len(list_of_pixels))
print(len(sequence_of_pixels))
    