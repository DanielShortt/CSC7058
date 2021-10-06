# Importing json module
import json

# opening json file (Stored in same directory as python file)
file = open('jsondata.json', "r")

# read the json data and store as json object
jsondata = json.loads(file.read())

#printing the full json file
print(jsondata)

#printing out an element of the json file
for i in jsondata['fruit']:
    print(i)

#closing the json file
file.close()

