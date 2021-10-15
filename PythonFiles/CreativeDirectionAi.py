import json

#Importing JSON Property File
print("Daz3D property file")
with open('Calibrated\ShotDeckUniqueID\DazImage001\CalibratedProperties\CalibratedDazProperties001.json') as file:
    Daz3DPropfile = json.load(file)

#Importing Soft Measurement
print("Soft Seasurements")
with open('SoftMeasurement\SM10001\SM10001.json') as file:
    SMFile = json.load(file)

#importing the user Selected Changes to soft measurement
print("User Selected Soft Measurements")
with open('Calibrated\ShotDeckUniqueID\DazImage001\SoftMeasurements\SSM10001.json') as file:
    SSMFile = json.load(file)

#Select Number of output variations
print("Selected number of Variations")
NumVariations = 5

#select output location
print("Output Location")
OutputLocation = ("EDIT THIS")

#RenderID for Variations
print("Unique ID")
RenderID = "RI10001"

#output 5X variations to stated output location
print("Output 5X Daz3D Properties")
with open ('D:\Software Masters\Year 3\AICinematographer\Calibrated\ShotDeckUniqueID\DazOutPut001\DazRender\Daz3DV1.json', 'w') as Daz3dV1:
    json.dump(Daz3DPropfile, Daz3dV1, indent=2)

#output 5X Soft Measurements 
print("Output Softmeasurements")
with open ('D:\Software Masters\Year 3\AICinematographer\Calibrated\ShotDeckUniqueID\DazOutPut001\DazRender\UserSM.json', 'w') as UserSM:
    json.dump(SSMFile, UserSM, indent=2)
