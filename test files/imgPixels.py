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
        
