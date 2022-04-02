import os, time, json
import subprocess
import ntpath
import argparse
from datetime import datetime
from genericpath import exists
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

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
        session.permanent = True
        user = request.form["labelLogin"]
        session["user"] = user
        flash("Login Successful.")
        return redirect(url_for("home", user = user))
    else: #if no post detected render homepage
        return render_template("index.html", imgAddress1 = image1, imgName1 = imageName1,
        imgAddress2 =image2, imgName2 = imageName2,
        imgAddress3 =image3, imgName3 = imageName3,
        imgAddress4 =image4, imgName4 = imageName4 )

#THE BROWSE PAGE.
@app.route("/browse")
def browse():
    return render_template("browse.html")  

#THE LABEL TOOL
@app.route("/label<image>") #label page passing in the image name.
def label(image):
    imageSelectedName = image
    imageSelected = "/static/Images/" + image
    return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName)


#THE LOGIN PAGE.  NOT REQUIRED AT THIS STAGE.
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
            session.permanent = True
            user = request.form["labelLoginModalButton"]
            session["user"] = user
            flash("Login Successful.")
            return redirect(url_for("user" ))
    else:
        if "user"in session:
            flash("Already logged in.")
            return redirect(url_for("user"))
        return render_template("login.html")

#THE RENDER PAGE. 
@app.route("/render<image>")
def renderimage(image):

    time.sleep(10)

    #properties file download from website
    propertyFile = "C:/Users/danie/Downloads/ImageProperties.txt"
    imageName = image
    now = datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    #outputFileName = imageName+str(timestamp)
    outputFileName = str(timestamp) #output name combination of time and date
    outputRenderName = outputFileName
    outputFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV3/app/static/imageProperties/"+outputFileName+".txt"

    #if property file exists rename and relocate to /static/imageProperties/
    if os.path.exists(propertyFile):
        os.rename("C:/Users/danie/Downloads/ImageProperties.txt", outputFileName)
        #CREATE SCRIPT TO REPLACE GENERIC TERMS WITH DAZ STUDIO ASSETS
        subprocess.Popen(['python', 'C:/Users/danie/Documents/GitHub/CSC7058/PythonFiles/parseProperties.py', outputFileName])
        ##########################################################################################

    #render location
    imageFileName = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/" + outputRenderName + ".jpg"
    imageFound = False
    renderCount = 0

    #check if image exists and relocate to /static/RenderLibrary/
    while not (imageFound):
        if os.path.exists(imageFileName):
            renderedImage = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV3/app/static/RenderLibrary/" + outputRenderName + ".jpg"
            os.rename(imageFileName, renderedImage)
            renderedImageMoved = "/static/RenderLibrary/" + outputRenderName + ".jpg"
            #renderedImage = imageFileName
            imageFound = True
            return render_template("render.html", content=renderedImageMoved, imageTitle = imageName, renderName = outputRenderName )  
        time.sleep(2.4)

    renderCount = renderCount +1

@app.route("/admin", methods=["POST","GET"])
def admin():

    if request.method == "POST":
        print("Nothing")

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
   
        
        adminMessagesLocation = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Admin/messages.txt"
        #Open the adminMessages file file.
        fileIn = open(adminMessagesLocation, "r")
        lines = fileIn.readlines()
        fileIn.close()

        return render_template("admin.html", messages = lines)

    else :
        adminMessagesLocation = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Admin/messages.txt"
        #Open the adminMessages file file.
        fileIn = open(adminMessagesLocation, "r")
        lines = fileIn.readlines()
        fileIn.close()

        return render_template("admin.html", messages = lines)


#THE MAIN FUNCTIONs
if __name__ == "__main__":
    app.run(debug=True)

 