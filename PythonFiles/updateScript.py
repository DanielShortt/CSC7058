import subprocess

genderInput = "Male"
expression = ""
clothingTop = ""
clothingBottom = ""

if (genderInput == "Female"):

    fileIn = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.txt", "rt")
    update = fileIn.read()

    update = update.replace('Male', 'Female')
    update = update.replace('Basic Wear T Shirt','Basic Wear Shorts')
    update = update.replace('Basic Wear Boxers','Basic Wear Tank Top')
    update = update.replace('Happy HD','Afraid HD')


    fileIn.close()

    fileOut = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.dsa", "wt")

    fileOut.write(update)

    fileIn.close()
    fileOut.close()


if (genderInput == "Male"):

    fileIn = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.txt", "rt")
    update = fileIn.read()

    update = update.replace('Female', 'Male')
    update = update.replace('Basic Wear Shorts','Basic Wear T Shirt')
    update = update.replace('Basic Wear Tank Top', 'Basic Wear Boxers')
    update = update.replace('Afraid HD', 'Happy HD')


    fileIn.close()

    fileOut = open("C:\\Daz 3D\\Applications\\Data\\DAZ 3D\\My DAZ 3D Library\\Scripts\\Shortt\\testScript.dsa", "wt")

    fileOut.write(update)

    fileIn.close()
    fileOut.close()

#Setting program .exe path to a variable 
dazStart = "C:\\Daz 3D\\Applications\\64-bit\\DAZ 3D\\DAZStudio4\\DAZStudio.exe"

#Starting target program program
subprocess.call([dazStart])