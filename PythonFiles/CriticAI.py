import json
import argparse

#arguments
parser = argparse.ArgumentParser()
parser.add_argument('dazSceneSpec', help='The first cinema director output image after processing.')
parser.add_argument('userSoftMeasurement', help='The location of the softmeasurements provided by the user to alter the image.')
parser.add_argument('criticOuputLoc', help='Critic Output Location.')
parser.add_argument('variationCount', type = int,  help='The number of scene variations to be compared.')
parser.add_argument('uniqueID', help='Unique ID for scene variations.')

args = parser.parse_args()
count = args.variationCount

for i in range(count):

    dazSceneOpen = args.dazSceneSpec + "\\Daz3DProps" + args.uniqueID + str(i) + ".json"
    print(dazSceneOpen)

    #Opening scientific daz3d property json file
    with open(dazSceneOpen) as dazFile:
        Daz3DPropfile = json.load(dazFile)
        print(Daz3DPropfile)

    SMOpen = args.userSoftMeasurement + "\\UserSoftMeasurements" + args.uniqueID + str(i) + ".json"
    print(SMOpen)

    #opening the default soft measurements that represent this image
    with open(SMOpen) as SMfile:
       userSoftMeasurements = json.load(SMfile)
       print(userSoftMeasurements)

    criticOutput = args.criticOuputLoc + "\\criticComparison" + args.uniqueID + str(i)  + ".json"

    with open(criticOutput, 'w') as SMOut:
        criticOut = json.dump(userSoftMeasurements, SMOut, indent = 2)