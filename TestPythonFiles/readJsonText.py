import json

dazAssetListLoc = "C:/Daz 3D/Applications/Data/DAZ 3D/AssetRender/assets.json" #file location of daz asset list. OUTPUT FORMAT UNDECIDED. List is output by daz studio. ASSUME JSON.

fileIn = open(dazAssetListLoc, "rt")
dazAssets = fileIn.read()
fileIn.close()

assetData = json.load(dazAssets)

############ READ TEXT FILE LINE BY LINE
 
# writing to file
file1 = open('myfile.txt', 'w')
file1.writelines(L)
file1.close()
 
# Using readlines()
file1 = open('myfile.txt', 'r')
Lines = file1.readlines()