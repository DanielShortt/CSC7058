import subprocess, os, time, json, argparse, winreg, psutil

#arguments passed to script
parser = argparse.ArgumentParser()
parser.add_argument('sciSceneSpec', help='Location of label selections made by user.')
parser.add_argument('assetJSON', help='File path of JSON file containing asset file Paths')
parser.add_argument('imageName', help='Name of the render output by Daz Studio.')

args = parser.parse_args()
tempFileName = args.sciSceneSpec
unloadAssets = args.assetJSON

#Loading Asset JSON file
with open(unloadAssets) as file1:
    loadAssets = json.load(file1)

#Parsing Environment and character dictionaries
enviroAssets = loadAssets["Environment"][0]
charAssets = loadAssets["Character"][0]

#setting variables
scriptAssets = {} #store the keys of the environment and character
enviroCount = 0

#check if file is stored in the correct file location. File name will eventually be an argument passed in.
imageproperties = tempFileName

#Open the image properties file.
with open(imageproperties) as file1:
    imageproperties = json.load(file1)

#store the labels keys for both environment and character selection.
environmentKeys = imageproperties['Environment'][0]
characterKeys = imageproperties['Character'][0]

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
            #print(imageproperties['Environment'][0][x])
            #print(y)
            scriptAssets[x]=enviroAssets[y]
            #print(scriptAssets[x])
            #print("\n")

#getting and storing the values stored against each key in the Character section of the imported JSON file.
for x in characterKeys:
    for y in charAssets:
        if (imageproperties['Character'][0][x] == y ):
            scriptAssets[x]=charAssets[y]

#print(scriptAssets)

#########################################################################################################
##ADDING CHARACTER FILE PATHS

#store number of characters selected during labelling process.
numChars = imageproperties['Environment'][0]['numberChars']
charLoopCount = 0
charAssets = 0

#open render scene file.
fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Character.txt", "rt")
update = fileIn.read()

#if number of characters selected  > 0 start adding character information.
if(numChars > 0):
    charLoopCount = 1
    #print(numChars)
    for y in range(numChars):
        for x in characterKeys:
            #print(x)
            if(str(charLoopCount) in x and characterKeys[x]!=''):
                print(x)
                #print(characterKeys[x])
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
    fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - CharacterProcessed.txt", "wt")
    fileOut.write(update)
    fileIn.close()
    fileOut.close()

#need to add character creation script to render scene. Needs to be position after environment and before expression script.



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
            assetFilePath = enviroAssets[assetBaseName]
            assetFileName = os.path.basename(assetFilePath)
            assetFileName = assetFileName.replace('.duf', '')
            update = update.replace("//assetDAZ", assetFileName)
            #print(update)
        elif(i == "atmosphere"):
            #open expression file and store as updateExpression. Add this to render scene file to add expressions to characters.
            translateIn = open(scriptAssets[i], "rt")
            updateExpression = translateIn.read()
            tempExpression = ("//"+i+"DAZ")
            update = update.replace(tempExpression, updateExpression)
            #print(update)
        else:
            #add remaining environment asset relative file paths to render scene file.
            if(scriptAssets[i] != ''):
                tempReplace = scriptAssets[i]
                temp = (i+"DAZ")
                tempKeyE = '//' + i + '.'
                update = update.replace(tempKeyE, '')
                update = update.replace(temp, tempReplace)


if(numChars > 0):
    CharFilein = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - CharacterProcessed.txt", "rt")
    updateChar = CharFilein.read()
    tempChar = "//" + "charAssets"
    update = update.replace(tempChar, updateChar)



#ADDING THE FILE NAME TO THE SCRIPT FOR RENDER

tempRenderFileName = args.sciSceneSpec
renderFileName = os.path.basename(tempRenderFileName) 
renderFileName = renderFileName.replace('.txt', '')
update = update.replace('//RENDERNAME', renderFileName)
#print(renderFileName)

fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.dsa", "wt")
fileOut.write(update)
fileIn.close()
fileOut.close()


#set the daz studio startup script
reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/renderScene - Environment.dsa" #insert path of scene here.
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry

#start daz to create and render scene.
dazStart = "C:/Daz 3D/Applications/64-bit/DAZ 3D/DAZStudio4/DAZStudio.exe"
#Starting daz studio 
subprocess.Popen([dazStart])


#setting output location to check for image render
imageFound = False
outputRenderName = args.imageName
renderedImage = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/RenderLibrary/" + outputRenderName + ".jpg"

#while imageFound = false iterate through this loop
while not (imageFound):
    #if the image is found based on the above path then reset Daz Studio on launch script to ""
    #set imageFound to true
    if os.path.exists(renderedImage):
        #Reset the Daz Launch script to ""
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the 
        #get the element to be updated
        sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) 
        newPath = "" #insert path of scene here.
        winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
        winreg.CloseKey(sKey) #close the value
        winreg.CloseKey(reg) #close the registry
        imageFound = True 
        
        #close any Daz Studio processes.
        # Iterate over all running process
        for proc in psutil.process_iter():
            try:
                # Get process name & pid from process object.
                processName = proc.name()
                #processID = proc.pid #not required.
                #killing process from task manager to ensure no conflict with relaunching Daz Studio
                procname = "DAZStudio.exe"
                if proc.name() == procname:
                    proc.kill()
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
    time.sleep(2) #sleep for 2 seconds before checking again if file is created.

#set the daz studio startup script
reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "" #insert path of scene here.
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry
