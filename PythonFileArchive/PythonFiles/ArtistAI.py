import argparse
import json


#arguments
parser = argparse.ArgumentParser()
parser.add_argument('sciSceneSpec', help='The location of a scientific scene json file that will be used to create a Daz3D scene ')
parser.add_argument('sceneID', help='This should be a uniqueID.')
parser.add_argument('artistOuputLoc', help='The Artist file output location.')
parser.add_argument('variationCount', type = int,  help='The number of scene variations to be created.')
parser.add_argument('resultUniqueID', help='Unique ID for scene variations.')

args = parser.parse_args()

#Storing output location in a variable
outputLoc = args.artistOuputLoc

#Opening scientific daz3d json file
with open(args.sciSceneSpec) as file1:
    sciDaz3DPropfile = json.load(file1)

#Storing unique ID in a variable
uniqueID = args.resultUniqueID

#Storing number of variations in a variable
count = args.variationCount

#loop to go process number of scene variations
for i in range(count):

    #Process of scene will happen here
    #temp processing of file
    SciDaz3DPropfileProcessed = sciDaz3DPropfile

    #uniqueID for new Daz3D property file for output
    dazSceneLoc = (args.storage + "\\Daz3DProps" + uniqueID + str(i) + ".json")

    #Outputting new Daz3D scene file.
    with open(dazSceneLoc, 'w') as out:
            json.dump(SciDaz3DPropfileProcessed, out, indent=2)    