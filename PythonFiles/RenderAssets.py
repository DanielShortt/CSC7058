import subprocess, time, winreg, psutil, os, json



############################################################################
#Program that will start daz store the assets on local machine and then render out each asset.


############################################################################
#set the daz studio script that runs on launch

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "LIST OF ASSETS" #insert location of script that will collect list of assets here.
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry

############################################################################
#open Daz Studio and run above script

#Setting program .exe path to a variable 
dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"
#Starting daz studio 
subprocess.Popen([dazStart])
#print("Daz running")
time.sleep=(30)



############################################################################
#Kill daz process if daz asset file exists.

fileCreated = False
dazAssets = "DAZ ASSET FILE" #file path of daz asset file
#print(killFile)
while(fileCreated == False):
        
        #CHANGE PATH
        if os.path.isfile(dazAssets):
            #do something
            #print("FOUND THE FILE")
            time.sleep=(5)
            #print("Killing process")

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

            #Changing fileCreated boolean to True, will end loop
            fileCreated = True
        else:
            #print("No")
            time.sleep=(10)
    
#delay to let process kill command clear
time.sleep=(10) # Sleep for x seconds

############################################################################
#read in daz list of assets from above to this python script

dazAssetListLoc = "DAZ ASSETS FILE" #file location of daz asset list. OUTPUT FORMAT UNDECIDED. List is output by daz studio. ASSUME JSON.
fileIn = open(dazAssetListLoc, "rt")
dazAssets = fileIn.read()

############################################################################
#take above list and store in array

assetArray = []

#Take JSON file and add easy row to new python list.
with open('assets.json') as data_file:    
    assetData = json.load(data_file)
    for asset in assetData:
        #print('x')
        if '.duf' in asset:
            assetArray.append
            

############################################################################
#Check if progress file exists 

progressFilePath = 'C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/renderProgressFile.txt'
currentPos = 0

if os.path.isfile(progressFilePath):
    fileIn = open(progressFilePath, "rt")
    currentProgress = fileIn.readline()

    #if the progress file exists. Store the position of the currentProgress.
    #this is where the current process will start from if available - else start from beginning.

    for x in assetArray:
        if x == currentProgress:
            print("Temp progress check")
        else:
            currentPos+=1

    #CONTINUE HERE>>>   

############################################################################
#set start up script to render daz assets from list stored above

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "RENDER LIST OF ASSETS" #insert location of script that will RENDER list of assets here.
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry


############################################################################
#for loop to iterate through list of assets

for x in range (): #arrayLength

############################################################################
    #set relative path of current iteration
    relFilePath = x #set relative fil path for render

############################################################################
    #check relative file path for acceptable file extensiosn

    if '.duf' in relFilePath:
        #print('continue')

############################################################################
        #open daz studio
        dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"
        #Starting daz studio 
        subprocess.Popen([dazStart])
        print("Daz running")
        time.sleep=(60) #allow 60 seconds for the render


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


            #Kill Daz process


        ############################################################################  
        #create file if it doesn't exist or store file path of 
            #create progress fill

            #update file progress with relative file path of current asset being rendered.


            #Kill Daz process



