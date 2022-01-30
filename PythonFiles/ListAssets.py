import subprocess, time, winreg, psutil, os, json

############################################################################
#Program that will start daz studio,
#store the asset list on local machine 

############################################################################
#set the daz studio script that runs on launch

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
#insert location of script that will collect list of assets here.
newPath = "C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/ListDazAssets.dsa" 
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry

directory = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender" #Directory for store asset render files

#create directory if not exists
if not os.path.exists(directory):
    os.makedirs(directory)

fileCreated = False
dazAssets = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/assets.txt" #file path of daz asset file

############################################################################
#open Daz Studio and run above script

#Setting program .exe path to a variable 
dazStart = "C:/Daz 3D/Applications/64-bit/DAZ 3D/DAZStudio4/DAZStudio.exe"
#Starting daz studio 
subprocess.Popen([dazStart])
print("Daz running")
#time.sleep(30)

############################################################################
#Kill daz process if daz asset file exists.

while(fileCreated == False):
        #CHANGE PATH
        if os.path.isfile(dazAssets):
            #do something
            #print("FOUND THE FILE")
            time.sleep(5)
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
            time.sleep(10)
    
#delay to let process kill command clear
time.sleep(10) # Sleep for x seconds

############################################################################
#set the daz studio script that runs on launch to empty

reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #open the registry
sKey = winreg.OpenKey(reg, "SOFTWARE\DAZ\Studio4", 0 , winreg.KEY_ALL_ACCESS | winreg.KEY_WOW64_64KEY) #get the element to be updated
newPath = "" #Resetting the Script to load on launch to None
winreg.SetValueEx(sKey, 'StartupScene', '0' , winreg.REG_SZ, newPath) #set the new value
winreg.CloseKey(sKey) #close the value
winreg.CloseKey(reg) #close the registry               

############################################################################
#End