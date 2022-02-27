import os
import ntpath
from datetime import datetime
from genericpath import exists
from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta

app = Flask(__name__, template_folder='../flaskr/templates')
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route("/")
def home():
    imageSelected = "/static/Images/Best_Beaches_Surfing.jpg"

    imageSelectedName = ntpath.basename(imageSelected)
    imageSelectedName = os.path.splitext(imageSelectedName)[0]

    return render_template("index.html", imgAddress = imageSelected, imgName = imageSelectedName)

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

@app.route("/render<image>")
def renderimage(image):

    propertyFile = "C:/Users/danie/Downloads/ImageProperties.txt"
    imageName = image
    now = datetime.now()
    timestamp = str(now.strftime("%Y%m%d_%H-%M-%S"))
    #current_date_time = datetime.now()
    outputFileName = imageName+str(timestamp)
    if os.path.exists(propertyFile):
        os.rename("C:/Users/danie/Downloads/ImageProperties.txt", 
        "C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/"+outputFileName+".txt")

        #CREATE SCRIPT TO REPLACE GENERIC TERMS WITH DAZ STUDIO ASSETS

        #BOOT DAZ RENDER IMAGE

        #MOVE IMAGE TO RENDERED IMAGES WITHIN STATIC FOLDER

        renderedImage = "/static/renderedImage/renderTest.jpg"
        return render_template("render.html", content=renderedImage, imageTitle = imageName )

    


if __name__ == "__main__":
    app.run(debug=True)

 