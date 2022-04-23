import os, time, subprocess, ntpath, psutil, json
from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, request, session


app = Flask(__name__, template_folder='../flaskr/templates')
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


#THE HOME PAGE
@app.route("/", methods=["POST","GET"])
def home():


    #Trending images to display on homepage
    image1 = "/static/Images/Best_Beaches_Surfing.jpg"
    imageName1 = ntpath.basename(image1)
    image2 = "/static/Images/conjuring.jpg"
    imageName2 = ntpath.basename(image2)
    image3 = "/static/Images/Fast-Furious-Render.jpg"
    imageName3 = ntpath.basename(image3)
    image4 = "/static/Images/Sherlock-Holmes.jpg"
    imageName4 = ntpath.basename(image4)

    #If a search term is entered redirect to browse with search term as query.
    if request.method == "POST":
        searchTerm = request.form["searchBarHome"]
        return redirect(url_for("browse", search = searchTerm))

    else: #if no post detected render homepage
        return render_template("index.html", imgAddress1 = image1, imgName1 = imageName1,
        imgAddress2 =image2, imgName2 = imageName2,
        imgAddress3 =image3, imgName3 = imageName3,
        imgAddress4 =image4, imgName4 = imageName4 )

#THE BROWSE PAGE.
@app.route("/browse<search>")
def browse(search):

    searchResultsJSONfile = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/JSON/searchResults.json"
    with open(searchResultsJSONfile) as file1:
        searchResultsJSON = json.load(file1)

    #parse out the results for the search term.
    images= searchResultsJSON[search]
    searchResults = []

    #store image paths in an array
    for i in images:
        searchResults.append(i["image"])

    return render_template("browse.html", searchTerm = search, searchResults = searchResults)  

#THE LABEL TOOL
@app.route("/label<image>", methods=["POST","GET"]) #label page passing in the image name.
def label(image):

    #open JSON file contain label types and icon/image paths
    labelTypesSource = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/JSON/labelTypes.json"

    with open(labelTypesSource) as file1:
        labelTypes = json.load(file1)

    #Open JSON File containing label types and options
    labelsSource = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/JSON/labels.json"

    with open(labelsSource) as file2:
        theLabels = json.load(file2)

    
    #Storing the label types for the environment and characters into individual arrays
    envLabelTypes = labelTypes['Environment'][0]
    charLabelTypes = labelTypes['Character'][0]

    #storing lengths of the above arrays
    envLabelIcons =([""])*len(envLabelTypes)
    charLabelIcons = ([""])*len(charLabelTypes)

    #setting count values for each array of label types. Used to populate arrays
    envCount = 0
    charCount = 0

    #storing the keyword for each environment label type icon
    for i in envLabelTypes:
        envLabelIcons[envCount] = envLabelTypes[i]
        count = envCount +1

    #storing the path for each character label type image
    for i in charLabelTypes:
        charLabelIcons[charCount] = charLabelTypes[i]
        charCount = count +1

    
    #storing all label types and associate label options
    envLabels = theLabels['Environment'][0]
    charLabels = theLabels['Character'][0]

    #if page is posted to store suggestion to message .txt file. Will be displayed in admin page.
    if request.method == "POST":
        imageSelectedName = image
        imageSelected = "/static/renderLibrary/" + image

        #get string from input entered by user.
        userAssetRequest = request.form["assetSuggestion"]
        #open file containing messages to be displayed to admin. Would be a database table row.
        fileAssetAppend = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/Admin/messages.txt", "a")
        #add message to file.Write.Close.
        fileAssetAppend.write(userAssetRequest  + "\n") 
        fileAssetAppend.close()

        #Render label page
        return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName, envLabelTypes = envLabelTypes, 
                                envLabelIcons = labelTypes, theLabels = envLabels,
                                charLabelTypes = charLabelTypes, charLabels = charLabels)

    else: #if no post then render page normally.   
        imageSelectedName = image
        imageSelected = "/static/renderLibrary/" + image
        return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName, envLabelTypes = envLabelTypes, 
                                envLabelIcons = labelTypes, theLabels = envLabels,
                                charLabelTypes = charLabelTypes, charLabels = charLabels)

#THE RENDER PAGE. 
@app.route("/render")
def renderimage():

    #ensuring process of the JavaScript has completed.
    time.sleep(1)

    #properties file download from website
    propertyFile = "C:/Users/danie/Downloads/ImageProperties.txt"
    #Creating file name for image and properties files.
    now = datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    outputFileName = str(timestamp) #output name combination of time and date
    outputRenderName = outputFileName
    #path to relocate impage properties file after download
    outputFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/imageProperties/"+outputFileName+".txt"
    #JSON file containing all possible asset relative file paths
    assetJSON = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/JSON/assetFilePath.json"

    #if property file exists rename and relocate to /static/imageProperties/
    if os.path.exists(propertyFile):
        os.rename("C:/Users/danie/Downloads/ImageProperties.txt", outputFileName)
        #CREATE SCRIPT TO REPLACE GENERIC TERMS WITH DAZ STUDIO ASSETS
        subprocess.Popen(['python', 
        'C:/Users/danie/Documents/GitHub/CSC7058/PythonFiles/parseProperties.py',  outputFileName, assetJSON, outputRenderName])
        ##########################################################################################

    #render location straight from Daz Studio
    imageFileName = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/" + outputRenderName + ".jpg"
    imageFound = False

    #check if image exists and relocate to /static/RenderLibrary/
    while not (imageFound):
        if os.path.exists(imageFileName):
            for proc in psutil.process_iter():
                try:
                    # If image has been found. End Daz Studio task. Get process name & pid from process object.
                    processName = proc.name()
                    #killing process from task manager to ensure no conflict with relaunching Daz Studio
                    procname = "DAZStudio.exe"
                    if processName == procname:
                        proc.kill()
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass
            #New image path - relocate
            renderedImage = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058StoryBoardApp/app/static/RenderLibrary/" + outputRenderName + ".jpg"
            os.rename(imageFileName, renderedImage)
            #path of new image (Flask)
            renderedImageMoved = "/static/RenderLibrary/" + outputRenderName + ".jpg"
            imageFound = True
            #Render the render page - pass in new image and new image name.
            return render_template("render.html", content=renderedImageMoved, renderName = outputRenderName )  
        time.sleep(2.4)



#THE MAIN FUNCTIONs
if __name__ == "__main__":
    app.run(debug=True)

 