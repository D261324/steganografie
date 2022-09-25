import imp
import re
import methodes

print('          __                                                         _____.__        ')
print('  _______/  |_  ____   _________    ____   ____   ________________ _/ ____\__| ___   ')
print(' /  ___/\   __\/ __ \ / ___\__  \  /    \ /  _ \ / ___\_  __ \__  \\   __\|  |/ __ \ ')
print(' \___ \  |  | \  ___// /_/  > __ \|   |  (  <_> ) /_/  >  | \// __ \|  |  |  \  ___/ ')
print('/____  > |__|  \___  >___  (____  /___|  /\____/\___  /|__|  (____  /__|  |__|\___  >')
print('     \/            \/_____/     \/     \/      /_____/            \/              \/ ')
print('                                                                             by 23hz ')
# askii art 
# start program
print('welkom bij de DE tool om jouw berichten te verstoppen in plain site')
print("maak een keuze uit welke resource je wilt gebruiken: ")

startKeuze = input("1. start met encoden \n2. start met decoderen\n maak een keuze: ")
s =  int(startKeuze)

if s == 1:
    methodes.encoding()
    
    
elif s == 2:
    methodes.decoding()
    
# 1. veranderingen doorlezen 
# 2. van losse werkende oplossingen een commit maken en omschrijven
# 3. her op pakken main
    
