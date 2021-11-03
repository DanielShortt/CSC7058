import subprocess

#scene variables. Inputs from 
genderInput = "Male"
expression = "Afraid HD"
filename = "VSCTest2"
clothingTorso = ""
clothingLegs = ""


#Update the gender to female with clothing and facial expression
if (genderInput == "Female"):

    #Open default script
    fileIn = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.txt", "rt")
    update = fileIn.read()

    #Update properties within script
    update = update.replace('GENDER', 'Female')
    update = update.replace('TORSOWEAR','Basic Wear Tank Top')
    update = update.replace('LEGSWEAR','Basic Wear Shorts')
    update = update.replace('EXPRESSION','Afraid HD')
    update = update.replace('INSERTNAME', filename)

    fileIn.close()

    #Open and write script updates to file
    fileOut = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.dsa", "wt")

    fileOut.write(update)

    fileIn.close()
    fileOut.close()

#Update the gender to female with clothing and facial expression
if (genderInput == "Male"):

    #Open default script
    fileIn = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.txt", "rt")
    update = fileIn.read()

    #Update properties within script
    update = update.replace('GENDER', 'Male')
    update = update.replace('TORSOWEAR','Basic Wear Boxers')
    update = update.replace('LEGSWEAR', 'Basic Wear T Shirt')
    update = update.replace('EXPRESSION', 'Happy HD')
    update = update.replace('INSERTNAME', filename)

    fileIn.close()

    #Open and write script updates to file
    fileOut = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.dsa", "wt")

    fileOut.write(update)

    fileIn.close()
    fileOut.close()

#Setting program .exe path to a variable 
dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"

#Starting target program program
subprocess.call([dazStart])