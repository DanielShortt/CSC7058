import os, time
import subprocess
import ntpath
from datetime import datetime
from genericpath import exists
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__, template_folder='../flaskr/templates')
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


#THE HOME PAGE
@app.route("/")
def home():
    image1 = "/static/Images/Best_Beaches_Surfing.jpg"
    imageName1 = ntpath.basename(image1)
    image2 = "/static/Images/conjuring.jpg"
    imageName2 = ntpath.basename(image2)
    image3 = "/static/Images/fast-furious.jpg"
    imageName3 = ntpath.basename(image3)
    image4 = "/static/Images/Sherlock-Holmes.jpg"
    imageName4 = ntpath.basename(image4)

    return render_template("index.html", imgAddress1 = image1, imgName1 = imageName1,
     imgAddress2 =image2, imgName2 = imageName2,
     imgAddress3 =image3, imgName3 = imageName3,
     imgAddress4 =image4, imgName4 = imageName4 )


#THE LABEL TOOL
@app.route("/label<image>")
def label(image):
    imageSelectedName = image

    imageSelected = "/static/Images/" + image


    return render_template("label.html", imgAddress = imageSelected, imgName = imageSelectedName)


#THE LOGIN PAGE.  NOT REQUIRED AT THIS STAGE.
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
            session.permanent = True
            user = request.form["nm"]
            session["user"] = user
            flash("Login Successful.")
            return redirect(url_for("user"))
    else:
        if "user"in session:
            flash("Already logged in.")
            return redirect(url_for("user"))
        return render_template("login.html")

#THE RENDER PAGE. FOR EXAMPLE ONLY.
@app.route("/render<image>")
def renderimage(image):

    propertyFile = "C:/Users/danie/Downloads/ImageProperties.txt"
    imageName = image
    now = datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    #current_date_time = datetime.now()
    outputFileName = imageName+str(timestamp)
    outputRenderName = outputFileName
    outputFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/"+outputFileName+".txt"


    if os.path.exists(propertyFile):
        os.rename("C:/Users/danie/Downloads/ImageProperties.txt", outputFileName)

        #CREATE SCRIPT TO REPLACE GENERIC TERMS WITH DAZ STUDIO ASSETS

        subprocess.Popen(['python', 'C:/Users/danie/Documents/GitHub/CSC7058/TestPythonFiles/testJson.py', outputFileName])

        #BOOT DAZ RENDER IMAGE

        #MOVE IMAGE TO RENDERED IMAGES WITHIN STATIC FOLDER


        ############################################################################################################################
        # renderedImage = "/static/renderedImage/renderTest.jpg"
        # return render_template("render.html", content=renderedImage, imageTitle = imageName )

    imageFileName = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/" + outputRenderName + ".jpg"
    #imageFileName = "/static/RenderLibrary/"+ outputRenderName + ".jpg"
    #imageFileName = "C:/Daz 3D/Applications/Data/DAZ 3D/Render Library/found.jpg"
    #fullImageFileName = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/RenderLibrary/found.jpg"
    #imageFileName = "/static/Images/Best_Beaches_Surfing.jpg"
    #imageFileName = "/static/RenderLibrary/found.jpg"

    imageFound = False
    renderCount = 0

    while not (imageFound):

        #flash(f"Rendering Image. Please wait. {renderCount}")

        if os.path.exists(imageFileName):
            renderedImage = "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/RenderLibrary/" + outputRenderName + ".jpg"
            os.rename(imageFileName, renderedImage)
            renderedImageMoved = "/static/RenderLibrary/" + outputRenderName + ".jpg"
            #renderedImage = imageFileName
            imageFound = True
            return render_template("render.html", content=renderedImageMoved, imageTitle = imageName )  
        # else:
        #     renderedImage = "/static/" + "loading.png"
        #     return render_template("render.html", content=renderedImage, imageTitle = "Loading Image." )


        


        time.sleep(2.4)

        ############ WORKING #### COMMENTED OUT ####### FOR TESTING ###############
    # if os.path.exists(imageFileName):
    #     renderedImage = imageFileName
    #     imageFound = True
    #     return render_template("render.html", content=renderedImage, imageTitle = imageName )  

    renderCount = renderCount +1


#THE MAIN FUNCTIONs
if __name__ == "__main__":
    app.run(debug=True)

 