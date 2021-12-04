import subprocess, time, winreg, psutil, os, json

############################################################################
#Program that will start daz studio,
#and render assets from asset list created by ListAssets.py.

############################################################################
#set the daz studio script that runs on launch

directory = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender" #Directory of Render output information.
dazAssets = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/assets.txt" #file path of daz asset file


############################################################################
#read in daz list of assets from ListAssets.py to this python script

dazAssetListLoc = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/assets.txt" #file location of daz asset list. OUTPUT FORMAT UNDECIDED. List is output by daz studio. ASSUME JSON.
fileIn = open(dazAssetListLoc, "r")
lines = fileIn.readlines()
fileIn.close()

############################################################################
#take above list and store in array

assetArray = []

#Take asset list txt file and add each row to new python list.

for line in lines:
    #print('x')
    if '.duf' in line:
        line = line.strip() #removing any return characters in string
        assetArray.append(line) #adding string to array

        

#store array in text file. Test only.
arrayFile = open(directory + '/' + 'arrayTest.txt', 'w')
for item in assetArray:
    arrayFile.write("%s\n" % item)
arrayFile.close()

#print("TEST ARRAY STORED AND WRITTEN TO FILE.")
            
############################################################################
#Check if progress file exists 

#the path to the progress file
progressFilePath = 'C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/renderProgressFile.txt'
currentPos = 0


if os.path.isfile(progressFilePath):

    fileIn = open(progressFilePath, "rt")
    currentProgress = fileIn.readline()
    currentProgress = currentProgress.strip()
    fileIn.close()
    #if the progress file exists. Store the position of the currentProgress.
    #this is where the current process will start from if available - else start from beginning.

    for x in assetArray:
        if x == currentProgress:
            #print("Temp progress check")
            currentPos+=1
            break
        else:
            currentPos+=1
else:
    #create file
    newFile = open(progressFilePath, 'w+')
    newFile.close()


############################################################################
#set start up script to render daz assets from list stored above

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/RenderAsset.dsa" #insert location of script that will RENDER list of assets here.
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry

print("ASSET RENDER SCRIPT SET.")

############################################################################
#for loop to iterate through list of assets

#start from currentPos (calculated above) in array and iterate through each item
for x in range (currentPos, len(assetArray)): #arrayLength
    #time.sleep(60.0)
############################################################################
    #set relative path of current iteration
    relFilePath = assetArray[x] #set relative file path for render
    relFilePath = relFilePath.strip()
    fileName = os.path.basename(relFilePath)
    fileName = fileName.replace('.duf', '')
    fileName = fileName.strip()

    print(fileName)

############################################################################
    #check relative file path for acceptable file extensiosn

    if '.duf' in relFilePath:
        print('DUF IN FILENAME')

    ############################################################################
        #update script to render asset with relative file path
        fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/RenderAsset.txt", "rt")
        update = fileIn.read()
        #Update properties within script
        update = update.replace('FILEPATH', relFilePath)
        update = update.replace('FILENAME', fileName)
        fileIn.close()

        #Open and write script updates to file
        fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/RenderAsset.dsa", "wt")

        fileOut.write(update)

        fileIn.close()
        fileOut.close()

        #Check for Renderfolder, Create if not exist.

        renderDirectory = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/Renders"
        renderedFile = renderDirectory + "/" + fileName

        if not os.path.exists(renderDirectory):
            os.makedirs(renderDirectory)

        #time.sleep(10)

    
        print("ABOUT TO RENDER")

        #time.sleep(10)
    ############################################################################
        #open daz studio
        dazStart = "C:/Daz 3D/Applications/64-bit/DAZ 3D/DAZStudio4/DAZStudio.exe"
        #Starting daz studio 
        subprocess.Popen([dazStart])
        #print("Daz running")
        renderCount = 0
        renderFound = False
        while(renderCount < 6): #60 time limit to open and render file before Daz is closed. Items not rendered added to error list

            if os.path.isfile(renderedFile):
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
                
                renderFound = True
                break

            else:
                renderCount+=1
                time.sleep(10)
        #time.sleep(100) #allow 60 seconds for the render

        #store relative file path of files not rendered
        if(renderFound == False):
            file = open(directory + '/' + 'renderErrors.txt', 'a') #create file and record relative file paths of renders not created.
            file.write(relFilePath  + "\n") 
            file.close()

############################################################################
        #open daz character
            #done in daz studio script
############################################################################
        #load daz asset
            #done in daz studio script
############################################################################
        #render asset and save
            #done in daz studio script


############################################################################
        #check if current progress location file exists

        #update file progress with relative file path of current asset being rendered.
        file = open(progressFilePath, 'r+')
        file.truncate(0) #clear out file
        file.close()

        with open(progressFilePath, 'a') as file:
            file.write(relFilePath) #write most recent file worked on
            file.close()

        #Kill Daz process

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


############################################################################
#set the daz studio script that runs on launch to empty

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "" #Resetting the Script to load on launch to NULL
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry               

############################################################################
#End


