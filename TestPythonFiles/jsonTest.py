import json

f = open('C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/JSON/labels.json')
data = json.load(f)

for i in data['Environment'][0]['Time'][0]:
    if(i == "Twilight"):
        print('in')
        fileIn = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/flaskr/templates/label.html", "r")
        update = fileIn.read()

        fileInUpdate = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Update/updateLabels.txt", "r")
        twilightLabel = fileInUpdate.read()

        if("<!-- PLACE NEW LABEL HERE -->" in update):
            update = update.replace("<!-- PLACE NEW LABEL HERE -->", twilightLabel)
        

        fileOut = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/flaskr/templates/label.html", "wt")
        fileOut.write(update)
        
        fileIn.close()
        fileInUpdate.close()
        fileOut.close()