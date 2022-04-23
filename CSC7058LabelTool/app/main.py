import os, time, json, ntpath, subprocess
from datetime import datetime, timedelta
from flask import Flask, redirect, url_for, render_template, request, session, flash

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
@app.route("/label<image>", methods=["POST","GET"]) #label page passing in the image name.
def label(image):

    if request.method == "POST":
        imageSelectedName = image
        imageSelected = "/static/Images/" + image

        #get string from input entered by user.
        userAssetRequest = request.form["assetSuggestion"]

        #open file containing messages to be displayed to admin. Would be a database table row.
        fileAssetAppend = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Admin/messages.txt", "a")

        #add message to file.Write.Close.
        fileAssetAppend.write(userAssetRequest  + "\n") 
        fileAssetAppend.close()

        return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName)

    else:    
        imageSelectedName = image
        imageSelected = "/static/Images/" + image
        return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName)

@app.route("/admin", methods=["POST","GET"])
def admin():

    #IF a post has been made to this page - i.e. an admin has update the JSON file containing the labels.
    if request.method == "POST":

        #open the labels file 
        f = open('C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/JSON/labels.json')
        data = json.load(f)

        #go through the labels checking for updates - in this case a specific word "Twilight" under the Enviroment section of the 
        # JSON file.
        for i in data['Environment'][0]['Time'][0]:
            if(i == "Twilight"):
                
                #Open the Labels HTML Page
                fileIn = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/flaskr/templates/label.html", "r")
                update = fileIn.read()

                #open the base label file. This will be the template div for a label selection.
                fileInUpdate = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Update/updateLabels.txt", "r")
                tempLabel = fileInUpdate.read()

                #Set the updateparameter name to lower case and replace keyword.
                iLower = (i.lower())
                tempLabel = tempLabel.replace('//UPDATENAME-LOWERCASE', iLower)

                #Replace keywork with update paramenter
                tempLabel = tempLabel.replace('//UPDATENAME', i)
                
                
                tempImage = data['Environment'][0]['Time'][0][i]

                #set icon/image for new label as set by admin
                tempLabel = tempLabel.replace('//UPDATEICON', tempImage)

                
                #place updated label div in label html file.
                if("<!-- PLACE NEW LABEL HERE -->" in update):
                    update = update.replace("<!-- PLACE NEW LABEL HERE -->", tempLabel)
                
                #store and close files
                fileOut = open("C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/flaskr/templates/label.html", "wt")
                fileOut.write(update)
                
                fileIn.close()
                fileInUpdate.close()
                fileOut.close()
   
        
        adminMessagesLocation = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058LabelTool/app/static/Admin/messages.txt"
        #Open the adminMessages file.
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



@app.route("/logout", methods=["POST","GET"])
def logout():
    if session is not None:
        #clear the session set in place when user logged in.
        session.clear()
        return redirect(url_for("home"))
    else:
        return url_for("home" )


#THE MAIN FUNCTIONs
if __name__ == "__main__":
    app.run(debug=True)

 