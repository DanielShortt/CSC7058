testArray = []

testListLoc = "C:/Daz 3D/Applications/Data/DAZ 3D/renderAssetsTestFile/testList.txt"
fileIn = open(testListLoc, "rt")
lines = fileIn.readlines()

#print(lines)

for line in lines:
    if '.duf' in line:
        testArray.append(line)

for line in testArray:
    print(line)