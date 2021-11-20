import subprocess
import time
############################################################################
#Set startup script to find and store daz assets relative file paths into a list

fileIn = open("", "rt")
updateStartupScript = fileIn.read()

#Update startup scirpt 
updateStartupScript = updateStartupScript.replace('',  '') #script path to be replaced     #new script path
fileIn.close()

#Open and write script updates to file
fileOut = open("", "wt") #output new daz studio program startscript with updated script to start upon program startup. clear as mud.
fileOut.write(updateStartupScript)
fileIn.close()
fileOut.close()





############################################################################
#open Daz Studio and run above script

#Setting program .exe path to a variable 
dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"
#Starting daz studio 
subprocess.Popen([dazStart])
print("Daz running")
time.sleep=(5)

############################################################################
#read in daz list of assets from above to this python script

dazAssets = "" #file location of daz asset list. OUTPUT FORMAT UNDECIDED.
fileIn = open(dazAssets, "rt")
updateStartupScript = fileIn.read()

############################################################################
#set start up script to render daz assets from list stored above

fileIn = open("", "rt")
updateStartupScript = fileIn.read()

#Update startup scirpt 
updateStartupScript = updateStartupScript.replace('',  '') #script path to be replaced     #new script path
fileIn.close()

#Open and write script updates to file
fileOut = open("", "wt") #output new daz studio program startscript with updated script to start upon program startup. clear as mud.
fileOut.write(updateStartupScript)
fileIn.close()
fileOut.close()

############################################################################
#for loop to iterate through list of assets

#need to convert input data into an array?

for x in range (): #arrayLength
    print("lol") #remove error until real code is input


############################################################################
    #set relative path of current iteration
    relFilePath = x #set relative fil path for render

############################################################################
    #check relative file path for acceptable file extensiosn

    if '.duf' in relFilePath:
        print('continue')

############################################################################
        #open daz studio
        dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"
        #Starting daz studio 
        subprocess.Popen([dazStart])
        print("Daz running")
        time.sleep=(5)


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



          ############################################################################  
            #create file if it doesn't exist or store file path of 


