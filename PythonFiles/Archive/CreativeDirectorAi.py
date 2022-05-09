import argparse
import json

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('sciSceneSpec', help='Location of Scientific ')
parser.add_argument('defSoftMeasurements', help='File location containing default softmeasurements for the scene')
parser.add_argument('userSoftMeasurements', help='File location containing user selected softmeasurements for the scene')
parser.add_argument('variationCount', type = int,  help='The number of scene variations to be created.')
parser.add_argument('storage', help='Output location of scene variations.')
parser.add_argument('resultUniqueID', help='Unique ID for scene variations.')

args = parser.parse_args()

#Opening scientific daz3d property json file
with open(args.sciSceneSpec) as file1:
    Daz3DPropfile = json.load(file1)

#print(Daz3DPropfile)

#opening the default soft measurements that represent this image
with open(args.defSoftMeasurements) as file2:
    DefaultSoftMeasurements = json.load(file2)

#print(DefaultSoftMeasurements)

#opening the file with user selected soft measurements
with open(args.userSoftMeasurements) as file3:
    UserSelectedSM = json.load(file3)

#print(UserSelectedSM)

count = args.variationCount

#print(count)

#storage = "D:\Software Masters\Year 3\TestFiles\Daz3DProps2.json"

#storing output location as variable
WriteLoc = (args.storage)

#print(WriteLoc)

uniqueID = args.resultUniqueID

#print(uniqueID)


#OUTPUTS

#loop to output selected number of variations
for i in range(count):
    
    #uniqueID for daz spec output file
    writeLocDazSpec = (args.storage + "\\Daz3DProps" + uniqueID + str(i) + ".json")

    with open(writeLocDazSpec, 'w') as out:
        json.dump(Daz3DPropfile, out, indent=2)

    #uniqueID for soft measurement output file
    writeLocSM = (args.storage + "\\UserSoftMeasurements" + uniqueID + str(i) + ".json")

    with open(writeLocSM, 'w') as out:
        json.dump(UserSelectedSM, out, indent=2)        
