import subprocess
import os
import psutil
import time
import json
import argparse

# parser = argparse.ArgumentParser()
# parser.add_argument('sciSceneSpec', help='Location of Scientific ')
# parser.add_argument('defSoftMeasurements', help='File location containing default softmeasurements for the scene')
# parser.add_argument('userSoftMeasurements', help='File location containing user selected softmeasurements for the scene')
# parser.add_argument('variationCount', type = int,  help='The number of scene variations to be created.')
# parser.add_argument('storage', help='Output location of scene variations.')
# parser.add_argument('resultUniqueID', help='Unique ID for scene variations.')

#args = parser.parse_args()

imageSource = "C:/Users/danie/Downloads/ImageProperties.txt"
imageproperties = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/ImageProperties.txt"

import os
os.rename(imageSource, imageproperties)



with open(imageproperties) as file1:
    imageproperties = json.load(file1)




varNums = 2 #not zero indexed in this case
camNums = 10 #zero Index = camNums +2

for x in range (varNums):

    #scene variables.
    genderInput = ""
    expression = "Afraid HD"
    filename = "newTest" + str(x)
    clothingTorso = ""
    clothingLegs = ""

    #Update the gender to female with clothing and facial expression
    if ( x%2==0 ): #temp conditional
        genderInput = "Female"
        #Open default script
        fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/TestScriptIncCameraLoop.txt", "rt")
        update = fileIn.read()

        #Update properties within script
        update = update.replace('GENDER', genderInput)
        update = update.replace('TORSOWEAR','Basic Wear Tank Top')
        update = update.replace('LEGSWEAR','Basic Wear Shorts')
        update = update.replace('EXPRESSION','Afraid HD')
        update = update.replace('INSERTNAME', filename)

        fileIn.close()

        #Open and write script updates to file
        fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/TestScriptIncCameraLoop.dsa", "wt")

        fileOut.write(update)

        fileIn.close()
        fileOut.close()

    #Update the gender to female with clothing and facial expression
    if ( x%2==1 ): #temp conditional
        genderInput = "Male"
        #Open default script
        fileIn = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/TestScriptIncCameraLoop.txt", "rt")
        update = fileIn.read()

        #Update properties within script
        update = update.replace('GENDER', genderInput)
        update = update.replace('TORSOWEAR','Basic Wear Boxers')
        update = update.replace('LEGSWEAR', 'Basic Wear T Shirt')
        update = update.replace('EXPRESSION', 'Happy HD')
        update = update.replace('INSERTNAME', filename)

        fileIn.close()

        #Open and write script updates to file
        fileOut = open("C:/Daz 3D/Applications/Data/DAZ 3D/My DAZ 3D Library/Scripts/Shortt/TestScriptIncCameraLoop.dsa", "wt")

        fileOut.write(update)

        fileIn.close()
        fileOut.close()

    #Setting program .exe path to a variable 
    dazStart = "C:/Daz 3D/Applications/64-bit/DAZ 3D/DAZStudio4/DAZStudio.exe"

    #Starting target program program
    #changed from subprocess.call([dazStart]) to allow killing of process after a delay of X
    subprocess.Popen([dazStart])
    print("Daz running" + str(x))
    #os.system( 'C:/"Daz 3D"/Applications/64-bit/"DAZ 3D"/DAZStudio4/DAZStudio.exe')
    time.sleep=(5)
    #Sleep to allow Daz to load and render out file
    #time.sleep(400) # Sleep for 3 seconds

    #Check for file creation . Kill DAZ
    fileCreated = False
    killFile = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/" + filename + str(camNums) + ".jpg"
    print(killFile)
    while(fileCreated == False):
        
        #CHANGE PATH
        if os.path.isfile(killFile):
            #do something
            print("FOUND THE FILE")
            time.sleep=(5)
            print("Killing process" + str(x))

            # Iterate over all running process
            for proc in psutil.process_iter():
                try:
                    # Get process name & pid from process object.
                    processName = proc.name()
                    processID = proc.pid
                    #print(processName , ' ::: ', processID)
                    #kill process command

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