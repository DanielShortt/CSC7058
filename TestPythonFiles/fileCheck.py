import os

filename = "testFile0"

fileCreated = False

while(fileCreated == False):

    #CHANGE PATH
    if os.path.isfile("C:/Users/danie/Documents/DAZ 3D/Studio/Render Library/" + filename + ".png"):
        #do something
        print("FOUND THE FILE")
        fileCreated = True
    else:
        #print("No")
        sleeps=(10)
