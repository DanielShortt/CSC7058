import subprocess
import os
import psutil
import time
import json
import argparse

#Setting up access to asset relative file paths. Would be best positioned in a database.
enviroAssets = {'Day':'Presets/Lights/Day.duf',
                'Night':'Presets/Lights/Night.duf',
                'Beach':'Environments/Landscapes/Multiplane Cyclorama/Beach.duf',
                'Tomb':'Props/NGartplay/Staging Chamber Iray/SC !Half Set Back Wall OB Iray.duf',
                'Dark':'/Scene Builder/Starter Essentials/Bright Moonlight Lights.duf',
                'Dim':'Scene Builder/Starter Essentials/Dusk Lights.duf',
                'Bright':'Environments/Architecture/Motel/Scenes/Motel Lights/Motel Day Lights.duf',
                'Fear':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/atmosphere/ExpressionFear.txt',
                'Happy':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shorttatmosphere/ExpressionHappy.txt',
                'Sad':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/atmosphere/ExpressionSad.txt',
                'Desk':'Props/Z_Office_Collection/Desk/Z_Desk.duf',
                'Altar':'Props/NGartplay/Staging Chamber 3DL/SC Altar.duf',
                'Car':'Figures/Celica/Celica.duf',
                'Surf Board':"People/Genesis 2 Male/Clothing/Surf's Up Outfit and Board/Surf's Up SurfBoard.duf",
                'leftUpper':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObjectUpperLeft.txt',
                'centreUpper':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObjectUpperCentre.txt',
                'rightUpper':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObjectUpperRight.txt',
                'leftLower':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObjectLowerLeft.txt',
                #'centerLower':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObject',
                'rightLower':'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/Translations/TranslateObjectLowerRight.txt',
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

#Setting up access to asset relative file paths. Would be best positioned in a database.
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

#check if file is stored in the correct file location. File name will eventually be an argument passed in.
imageSource = "C:/Users/danie/Downloads/ImageProperties.txt" #needs renamed
imageproperties = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/ImageProperties.txt" #needs a renamed

#if file is exists move to image properties file. This is the file containing the labels selected on the web app.
if os.path.isfile(imageSource): 
    os.rename(imageSource, imageproperties)


#Open the image properties file.
with open(imageproperties) as file1:
    imageproperties = json.load(file1)

#store the labels keys for both environment and character selection.
environmentKeys = imageproperties['Environment'][0]
characterKeys = imageproperties['CharacterInfo'][0]

#Finding the number of environment labels. Used to ensure correct loop count.
for i in environmentKeys:
    if (environmentKeys[i] != "" ):
        enviroCount += 1

#removing 2 for unnecessary keys at this stage. An area that can be used to talk about during testing.
if(environmentKeys["numberChars"]>0):
    enviroCount -= 2

#getting and storing the values stored against each key in the environment section of the imported JSON file.
for x in environmentKeys:
    for y in enviroAssets:
        if (imageproperties['Environment'][0][x] == y ):
            scriptAssets[x]=enviroAssets[y]

#getting and storing the values stored against each key in the Character section of the imported JSON file.
for x in characterKeys:
    for y in charAssets:
        if (imageproperties['CharacterInfo'][0][x] == y ):
            scriptAssets[x]=charAssets[y]
            


###############################################################################################################
##ADDING Environment FILE PATHS to the Daz Script


#open the environment default daz script.
fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.txt", "rt")
update = fileIn.read()
for i in environmentKeys:
    if(environmentKeys[i] != "" and (i + 'DAZ') in update):

        #Updating the Key phrases stored in the script file with the relevant asset file paths.
        if(i == "propLoc"):
            #open the current translation file and add translation to render scene file.
            translateIn = open(scriptAssets[i], "rt")
            updateTrans = translateIn.read()
            tempTranslate = (i+"DAZ")
            update = update.replace(tempTranslate, updateTrans)
            #take name off main prop and add to designated location in script for translation
            assetBaseName = os.path.splitext(environmentKeys['mainProp'])[0]
            update = update.replace("//assetDAZ", assetBaseName)
            #print(update)
        elif(i == "atmosphere"):
            #open expression file and store as updateExpression. Add this to render scene file to add expressions to characters.
            translateIn = open(scriptAssets[i], "rt")
            updateExpression = translateIn.read()
            tempExpression = (i+"DAZ")
            update = update.replace(tempExpression, updateExpression)
            #print(update)
        else:
            #add remaining environment asset relative file paths to render scene file.
            tempReplace = scriptAssets[i]
            temp = (i+"DAZ")
            tempKeyE = '//' + i + '.'
            update = update.replace(tempKeyE, '')
            update = update.replace(temp, tempReplace)

fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.dsa", "wt")
fileOut.write(update)
fileIn.close()
fileOut.close()


########################################################################################################################################
##ADDING CHARACTER FILE PATHS

#store number of characters selected during labelling process.
numChars =  environmentKeys = imageproperties['Environment'][0]['numberChars']
charLoopCount = 0
charAssets = 0

#open render scene file.
fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Character.txt", "rt")
update = fileIn.read()

#if number of characters selected  > 0 start adding character informatio.
if(numChars > 0):
    charLoopCount = 1
    #print(numChars)
    for y in range(numChars):
        for x in characterKeys:
            #print(x)
            if(str(charLoopCount) in x and characterKeys[x]!=''):
                #add character information based on loop cound y. x will go through each asset for each relevant character.
                tempReplace = scriptAssets[x]
                temp = (x+"DAZ")
                tempKey = '//' + x + '.'
                update = update.replace(tempKey, '')
                update = update.replace(temp, tempReplace)
                charAssets += 1

                #x.replace('gender1.', '')   #USE TO REMOVE COMMENT OUT FROM SCRIPT.

        charLoopCount += 1
    update = update.replace("//charLoopX.", '') #uncommenting out the character loop value in the character script.
    update = update.replace("charLoopXDAZ", str(charAssets)) #setting the value for the loop.
    fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Character.dsa", "wt")
    fileOut.write(update)
    fileIn.close()
    fileOut.close()

    #need to add character creation script to render scene script. Needs to be position after environment and before expression script.