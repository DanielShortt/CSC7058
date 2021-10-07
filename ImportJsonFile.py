import json

#open json file and load into python objectWeek 25-36
with open('states.json') as file:
    jsondata = json.load(file)

#loop through python object to print data
for state in jsondata['states']:
    print(state['name'], state['abbreviation'])

#loop through object to delete the "area code"
for state in jsondata['states']:
 del state['area_codes']

#output update data to a new json file
#another comment to check on git
#another change
with open ('new_states.json', 'w') as f:
    json.dump(jsondata, f, indent=2)

