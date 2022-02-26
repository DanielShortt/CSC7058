import subprocess
import os
import psutil
import time
import json
import argparse

#store in external assets file
enviroAssets = {'Day':'Presets/Lights/Day.duf',
                'Night':'Presets/Lights/Night.duf',
                'Beach':'Environments/Landscapes/Multiplane Cyclorama/Beach.duf',
                'Tomb':'/filepath/forTomb/asset.lol',
                'Dark':'/Scene Builder/Starter Essentials/Bright Moonlight Lights.duf',
                'Dim':'Scene Builder/Starter Essentials/Dusk Lights.duf',
                'Bright':'Environments/Architecture/Motel/Scenes/Motel Lights/Motel Day Lights.duf',
                'Fear':'/filepath/forFear/asset.lol',
                'Happy':'/filepath/forHappy/asset.lol',
                'Sad':'/filepath/forSad/asset.lol',
                'Desk':'/filepath/forDesk/asset.lol',
                'Altar':'Props\NGartplay\Staging Chamber 3DL/SC Altar.duf',
                'Car':'/filepath/forCar/asset.lol',
                'Surf Board':"People\Genesis 2 Male\Clothing\Surf's Up Outfit and Board/Surf's Up SurfBoard.duf",
                'leftUpper':'/filepath/forUpperLeft/asset.lol',
                'centreUpper':'/filepath/forUpperCentre/asset.lol',
                'rightUpper':'/filepath/forUpperRight/asset.lol',
                'leftLower':'/filepath/forLowerLeft/asset.lol',
                'centerLower':'/filepath/forLowerCenter/asset.lol',
                'rightLower':'/filepath/forLowerRight/asset.lol',
                'FaceClose':'filepath/FaceClose',
                'Front':'filepath/Front',
                'IsoClose':'filepath/IsoClose',
                'TopLeftCam':'filepath/TopLeftCam',
                'TopRightCam':'filepath/TopRightCam',
                '0':'/filepath/for0/asset.lol',
                '1':'/filepath/for1/asset.lol',
                '2':'/filepath/for2/asset.lol',
                '3':'/filepath/for3/asset.lol',
                '4':'/filepath/for4/asset.lol'
                }

#store in external assets file
charAssets = {  'Male':'People/Genesis 8 Male/Genesis 8 Basic Male.duf',
                'Female':'People/Genesis 8 Female/Genesis 8 Basic Female.duf',
                'Long':'People/Genesis 8 Female/Hair/Reizibarrientos/TemperascencseNoelHair/NoelHair.duf',
                'Bob':'People/Genesis 8 Female/Hair/perlk/Bob haircut.duf',
                'Short':'People/Genesis 8 Male/Hair/Armani Hair/Armani Hair.duf',
                'Mohawk':'Runtime/Libraries/Character/AprilYSH/AprilGenesis/Ciri Hair.duf',
                'Shaved':'/filepath/forShaved/asset.lol',
                'Standing':'People/Genesis 8 Male/Poses/Base Poses/Base Pose Walking A.duf',
                'Sitting':'People/Genesis 8 Male/Poses/Base Poses/Base Pose Sitting C.duf',
                'Tshirt':'People/Genesis 8 Male/Clothing/Basic Wear/Basic Wear T Shirt.duf',
                'Shirt':'People/Genesis 8 Male/Clothing/Walther Wardrobe/WaltherShirt.duf',
                'Blouse':'People/Genesis 8 Female/Clothing/Most Digital Creations/G8F Plaid Shirt/G8F Plaid Shirt.duf',
                'Trousers':'People/Genesis 8 Male/Clothing/perlk/G8M Jeans/Open Fly Jeans.duf',
                'Shorts':'People/Genesis 8 Male/Clothing/Basic Wear/Basic Wear Boxers.duf',
                'Skirt':'People/Genesis 8 Female/Clothing/Rocker Outfit/Rocker Skirt.duf',
                'Sword':'Props/kalhh/sword-fantasy/sword.duf',
                'Gun':'Props/Backwoods Shooting Range/Hand Poses/Genesis 8 Male/Backwoods Shooting Range Rifle L Hand.duf',
                'Phone':'Props/GMS Props/Smartphone/G8M_Smartprop.duf'}

scriptAssets = {}
#imageproperties = "C:/Users/danie/Downloads/ImageProperties.txt"   
enviroCount = 0

imageSource = "C:/Users/danie/Downloads/ImageProperties.txt" #needs renamed
imageproperties = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/ImageProperties.txt" #needs a renamed

if os.path.isfile(imageSource): 
    os.rename(imageSource, imageproperties)



with open(imageproperties) as file1:
    imageproperties = json.load(file1)

environmentKeys = imageproperties['Environment'][0]
characterKeys = imageproperties['CharacterInfo'][0]

for i in environmentKeys:
    if (environmentKeys[i] != "" ):
        enviroCount += 1

if(environmentKeys["numberChars"]>0):
    enviroCount -= 2

for x in environmentKeys:
    for y in enviroAssets:
        if (imageproperties['Environment'][0][x] == y ):
            #print(imageproperties['Environment'][0][x])
            #print(y)
            scriptAssets[x]=enviroAssets[y] 

for x in characterKeys:
    for y in charAssets:
        if (imageproperties['CharacterInfo'][0][x] == y ):
            scriptAssets[x]=charAssets[y] 


###############################################################################################################
##ADDING Environment FILE PATHS

fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.txt", "rt")
update = fileIn.read()
for i in environmentKeys:
    if(environmentKeys[i] != "" and (i + 'DAZ') in update ):
        tempReplace = scriptAssets[i]
        temp = (i+"DAZ")
        update = update.replace(temp, tempReplace)
fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.dsa", "wt")
fileOut.write(update)
fileIn.close()
fileOut.close()


########################################################################################################################################
##ADDING CHARACTER FILE PATHS


numChars =  environmentKeys = imageproperties['Environment'][0]['numberChars']
charLoopCount = 0
charAssets = 0

fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Character.txt", "rt")
update = fileIn.read()


if(numChars > 0):
    charLoopCount = 1
    #print(numChars)
    for y in range(numChars):
        for x in characterKeys:
            #print(x)
            if(str(charLoopCount) in x and characterKeys[x]!=''):
                print(x)
                tempReplace = scriptAssets[x]
                temp = (x+"DAZ")
                tempKey = '//' + x + '.'
                update = update.replace(tempKey, '')
                update = update.replace(temp, tempReplace)
                charAssets += 1

                #x.replace('gender1.', '')   #USE TO REMOVE COMMENT OUT FROM SCRIPT.

        charLoopCount += 1

    update = update.replace("//charLoopX.", '') #setting the value for the loop
    update = update.replace("charLoopXDAZ", str(charAssets)) #setting the value for the loop
    fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Character.dsa", "wt")
    fileOut.write(update)
    fileIn.close()
    fileOut.close()