//START OF SCRIPTING FILES

//GLOBAL VARIABLES
var divShown = ""; //Stores the id of the current environment label type div shown
var charDivShown = ""; // stores the id of the current character label type shown
var charCount = 0, charTotal = 0; //stores the values for the max number of characters selected and current active character
var latestCharUpdated = 0; //the latest character that has had an update.
var CharLoopTitleId = "charNumTitle" //Character title.
var outputFile = ""; //the file used to store the label information selections for output in JSON information after 
var clickCount = 0; //used to count the number of variables selected/modified.

//Used to navigate the environment array
const environmentArrayTitles = ["time", "setting", "lighting", "atmosphere", "mainProp", "propLoc", "camera", "numberChars"];

//Used to navigate the character array
const characterArrayTitles = ['gender', 'charLoc', 'hair', 'pose', 'top', 'bottoms', 'prop'];

//used to store the environment label selections
const environmentArray = {
    'time': 'Night', 'setting': 'Beach', 'lighting': '', 'atmosphere': 'Sad',
    'mainProp': "Surfboard", 'propLoc': 'leftUpper', 'camera': '', 'numberChars': 1
};

//used to store the character label selections
const characterArray = {
    'gender1': 'Male', 'charLoc1': 'upperLeft', 'hair1': 'Short', 'pose1': 'Sitting', 'top1': 'TShirt', 'bottoms1': 'Shorts', 'props1': '',
    'gender2': '', 'charLoc2': '', 'hair2': '', 'pose2': '', 'top2': '', 'bottoms2': '', 'props2': '',
    'gender3': '', 'charLoc3': '', 'hair3': '', 'pose3': '', 'top3': '', 'bottoms3': '', 'props3': '',
    'gender4': '', 'charLoc4': '', 'hair4': '', 'pose4': '', 'top4': '', 'bottoms4': '', 'props4': ''
}; //End of array

//update the value of clickCount. Change the images displayed in display tool.
function clickCountIncrease() {
    clickCount++;
    for(let i = 0; i<3; i++){
        mainImage = "mainImage" + i
        //hide/show demo divs based on the value of i in the loop
        if (clickCount % 3 == i) {
            document.getElementById(mainImage).style.display = 'block';
        } else {
            document.getElementById(mainImage).style.display = 'none';
        }
    }
};

//FUNCTION TO SHOW DIV
function showDiv(divId, element) {
    if (divShown != "") {
        divHide("", divShown);
    }
    document.getElementById(divId).style.display = 'block';
    divShown = divId;
}

//FUNCTION TO HIDE DIV
function divHide(id, cara) {
    buttonid = id
    //console.log("buttonID selected" + buttonid) // used for debugging.
    var T = document.getElementById(cara);
    T.style.display = "none";  // <-- Set it to block
    divShown = "";
}

//FUNCTION TO SHOW CHRACTER CREATION DIVS
function showCharDiv(divId) {
    if (charDivShown != "") {
        hideCharDiv("", charDivShown);
    }

    document.getElementById(divId).style.display = 'block';
    charDivShown = divId;
}

//FUNCTION TO HIDE CHARACTER CREATION DIV
function hideCharDiv(id, cara) {
    buttonid = id
    //console.log("buttonID selected" + buttonid) // used for debugging.
    var T = document.getElementById(cara);
    T.style.display = "none";  // <-- Set it to block
    charDivShown = "";
}


//FUNCTION TO SET NUMBER OF CHARS SELECTED TO CONTROL LOOP 
//FUNCTION SETS UP DIVS FOR SETTING CHRACTER CREATION VARIABLES
function charInfo(numOfChars) {
    //Add Char info here.
    for (let i = 0; i < 5; i++) {
        if (numOfChars == "char" + i) {
            charTotal = i;
            addElement(i, "numberChars")
            document.getElementById("numCharBar").classList.remove("d-flex");
            document.getElementById('numCharBar').style.display = 'none';
        }
    }

    //If char total selected >0 then set character to appropriate value.
    if (charTotal > 0 && charCount < 1) {
        charCount += 1;
        latestCharUpdated = 1;
        var charLoopTitle = "Character " + charCount;
        var CharLoopTitleId = "charNumTitle"
        var updateCharLoopTitle = document.getElementById(CharLoopTitleId);
        updateCharLoopTitle.innerHTML = charLoopTitle;
        var charIdUpdate = "caraCharDetails" + charCount;
        document.getElementById("caraCharDetails").id = charIdUpdate;
        document.getElementById(charIdUpdate).style.display = 'block';
    } else if (charTotal = 0) {
        document.getElementById('caraNumChars').style.display = 'none';
    }
}

//FUNCTION WILL BE USED TO START THE PROCESS TO MODIFY NEXT CHARACTER
function nextChar() {
    //CREATE NEXT BUTTON. HIDE CURRENT DIVS. UPDATE DIV ID's. SHOW NEW DIVS.
    var charLoopTitle;
    var updateCharLoopTitle;
    if (charCount < charTotal) {
        charCount = charCount + 1;
        charLoopTitle = "Character " + charCount;
        updateCharLoopTitle = document.getElementById(CharLoopTitleId);
        updateCharLoopTitle.innerHTML = charLoopTitle;
        activeChar("characterLabelHeader" + charCount);
    }
}

function prevChar() {
    //CREATE NEXT BUTTON. HIDE CURRENT DIVS. UPDATE DIV ID's. SHOW NEW DIVS.
    var charLoopTitle;
    var updateCharLoopTitle;
    if (charCount == 1) {
        //do nothing
    } else {
        charCount = charCount - 1;
        charLoopTitle = "Character " + charCount;
        updateCharLoopTitle = document.getElementById(CharLoopTitleId);
        updateCharLoopTitle.innerHTML = charLoopTitle;
        activeChar("characterLabelHeader" + charCount);
    }
}



//FUNCTION TO PLACE SHADOW ON BUTTON ONCE PRESSED ************************* REMOVE?
function addShadow(id) {
    document.getElementById(id).style["boxShadow"] = "0 0 10px #000000";
}


//CREATING AND MODIFYING THE LABEL OBJECTS
//FUNCTION SETS THE OBJECT VARIABLES
function addElement(object, label) {

    var elementExists = false;
    var objectLabelId = "";
    var updateCara = "";

    if (label == "Time") {
        if (environmentArray['time'] != "") {
            elementExists = true;
        }
        environmentArray['time'] = object;
        objectLabelId = "timeId";
        updateCara = "caraTime";

    } else if (label == "Setting") {
        if (environmentArray['setting'] != "") {
            elementExists = true;
        }
        environmentArray['setting'] = object;
        objectLabelId = "settingId";
        updateCara = "caraSetting";

    } else if (label == "Lighting") {
        if (environmentArray['lighting'] != "") {
            elementExists = true;
        }
        environmentArray['lighting'] = object;
        objectLabelId = "lightingId";
        updateCara = "caraLighting";

    } else if (label == "Atmosphere") {
        if (environmentArray['atmosphere'] != "") {
            elementExists = true;
        }
        environmentArray['atmosphere'] = object;
        objectLabelId = "atmosphereId";
        updateCara = "caraAtmosphere";

    } else if (label == "MainProp") {
        if (environmentArray['mainProp'] != "") {
            elementExists = true;
        }
        environmentArray['mainProp'] = object;
        objectLabelId = "propId";
        updateCara = "caraMainProp";

    } else if (label == "PropLoc") {
        if (environmentArray['propLoc'] != "") {
            elementExists = true;
        }
        environmentArray['propLoc'] = object;
        objectLabelId = "propLocId";
        updateCara = "caraPropLoc";

    } else if (label == "Camera") {
        if (environmentArray['camera'] != "") {
            elementExists = true;
        }
        environmentArray['camera'] = object;
        objectLabelId = "cameraId";
        updateCara = "caraCamera";

    } else if (label == "numberChars") {
        if (environmentArray['numberChars'] != "") {
            elementExists = true;
        }
        environmentArray['numberChars'] = charTotal;
        objectLabelId = "numberCharsId";
        updateCara = "caraNumChars";
    }


    if (elementExists == false) {

        // create a new div element
        const newDiv = document.createElement("div");
        newDiv.className = "row anObject";
        //newDiv.id = objectLabelId;
        newDiv.setAttribute("onclick", "showDiv('" + updateCara + "', 1)");

        //new inner div for label
        const newDiv1 = document.createElement("div");
        newDiv1.className = "objectTitle";

        //new label for outter div
        const newLabel = document.createElement("label");
        newLabel.id = objectLabelId;
        const newLabel1 = document.createElement("label");
        newLabel1.className = "labelType";


        //and give it some content
        const objectID = document.createTextNode(object);
        const objectLabel = document.createTextNode(label);

        //appending labels to div
        newLabel.appendChild(objectID);
        newLabel1.appendChild(objectLabel);

        // add the text node to the newly created div
        newDiv.appendChild(newDiv1);
        newDiv1.appendChild(newLabel);
        newDiv1.appendChild(newLabel1);


        // add the newly created element and its content into the DOM
        const currentDiv = document.getElementById("insertObjects");
        const parentDiv = document.getElementById("objects");
        parentDiv.insertBefore(newDiv, currentDiv.nextSibling);
        clickCountIncrease();


    } else {
        //update property already selected to new value selected by user
        document.getElementById(objectLabelId).innerHTML = object;
        clickCountIncrease();
        elementExists = false;
    }
}


//Create the character Labels and store them in global variables above
//labels stored in labels column under character header   
function addCharElement(object, label) {

    console.log(object, label) // WORKING HERE
    //high level variables required for function
    var temp = "";
    var objectLabelId = "";
    var objectLabelId = "";
    var newCharDiv = "";
    var elementExists = false, charExists = false;
    var charClassTitle = "charLabels" + charCount; 

    //Create new High level character label divs
    if (document.getElementById(charClassTitle)) {
        charExists = true
        latestCharUpdated = charCount;
    } else {
        newCharDiv = document.createElement("div");
        newCharDiv.className = charClassTitle; // row charLabels1
        newCharDiv.id = charClassTitle;
        const newLabel = document.createElement("label");
        newLabel.className = "characterLabelHeader" + charCount;
        newLabel.id = "characterLabelHeader" + charCount;
        newLabel.setAttribute("onclick", "activeChar(this.id),showDiv('caraNumChars')"); //activeChar(id)
        const objectLabel = document.createTextNode("Character " + charCount);
        newLabel.appendChild(objectLabel);
        newCharDiv.appendChild(newLabel);
        
    }

    //Position new div under the character labels in left column
    if (charCount == 1 && !charExists) {
        // add the newly created element and its content into the DOM
        const currentDiv = document.getElementById("insertCharObjects");
        const parentDiv = document.getElementById("charObjects");
        parentDiv.insertBefore(newCharDiv, currentDiv.nextSibling);
    } else if (charExists) {
        //do nothing
    } else { // POSITION charLabels2 AFTER charLabels1 etc
        const currentDiv = document.getElementById("charLabels" + (latestCharUpdated));
        const parentDiv = document.getElementById("charObjects");
        parentDiv.insertBefore(newCharDiv, currentDiv.nextSibling);
        latestCharUpdated = charCount;
    }

    //END OF TEST


    if (charCount > 0) {
        temp = label + charCount  //eg gender1
    }
    console.log(temp)
    var item = characterArray[temp];
    
    if (item != '') {
        console.log("WHY AM I IN HERE?")
        elementExists = true;
    }

    //Looking  in character array and storing value for label + current active character number
    characterArray[temp] = object;
    objectLabelId = temp + "id";

    //if element does not exist create a new element and popluate active character
    if (elementExists == false) {
        console.log("SHOULD BE IN HERE")
        //console.log("About to create a new Character element");

        // create a new div element
        const newDiv = document.createElement("div");
        newDiv.className = "row aCharacterObject" + charCount;
        newDiv.id = "aCharacterObject" + charCount;
        newDiv.style.display = "block";
        newDiv.setAttribute("onclick", "showDiv('caraNumChars',1), activeChar(this.id),showCharDiv('" + label + "')"); //activeChar(id)
        // newDiv.onclick=""; Create NEW function to modify selected settings. <--------------------------------------------

        const newDiv1 = document.createElement("div");
        newDiv1.className = "charObjectTitle";

        const newLabel = document.createElement("label");
        newLabel.id = objectLabelId;
        const newLabel1 = document.createElement("label");
        newLabel1.className = "labelType";


        // and give it some content
        const objectID = document.createTextNode(object);
        const objectLabel = document.createTextNode(label);

        newLabel.appendChild(objectID);
        newLabel1.appendChild(objectLabel);

        // add the text node to the newly created div
        newDiv.appendChild(newDiv1);
        newDiv1.appendChild(newLabel);
        newDiv1.appendChild(newLabel1);
        clickCountIncrease();
        // add the newly created element and its content into the DOM
        const currentDiv = document.getElementById("charLabels" + charCount).appendChild(newDiv);

    } else { // else update element that already exists with new selection
        document.getElementById(objectLabelId).innerHTML = object;
        clickCountIncrease();
        elementExists = false;
    }
}


//CODE to show/hide active and inactive char creation.
function activeChar(id) {

    var activeChar1 = document.getElementsByClassName("aCharacterObject1");
    var activeChar2 = document.getElementsByClassName("aCharacterObject2");
    var activeChar3 = document.getElementsByClassName("aCharacterObject3");
    var activeChar4 = document.getElementsByClassName("aCharacterObject4");
    const activeChars= [activeChar1, activeChar2, activeChar3, activeChar4]

    for (let i = 0; i < charTotal; i++) {
        let activeChar = activeChars[i]
        let activeCharValue = (i+1) //As i beings at Zero
        for(let j =0; j< activeChar.length; j++){
            if (id == "characterLabelHeader" + activeCharValue || id == "aCharacterObject" + activeCharValue) {
                updateCurrentChar(activeCharValue);
                activeChar[j].style.display = "block";
            } else {
                activeChar[j].style.display = "none";
            }
        }
    }
}

//updating current char number title and global variable charCount
function updateCurrentChar(char) {
    var charLoopTitle;
    var updateCharLoopTitle;
    charLoopTitle = "Character " + char;
    updateCharLoopTitle = document.getElementById(CharLoopTitleId);
    updateCharLoopTitle.innerHTML = charLoopTitle;
    charCount = char;
}

//NEED TO LOAD JSON FILE.
function loadJSON() {
    //temp method to load in JSON. Need to figure out how to modify data loaded in.
    fetch('static/JSON/scene.json')
        .then(response => response.json())
        .then(data => {

            //Store number of scene properties selected
            var count = Object.keys(data.Environment[0]).length;
            //Store number of character properties selected
            var countC = characterArrayTitles.length;

            //storing scene titles to dictionary
            for (let i = 0; i < count; i++) {
                data.Environment[0][environmentArrayTitles[i]] = environmentArray[environmentArrayTitles[i]];
                //console.log(data.Environment[0][environmentArrayTitles[i]]);
            }

            //storing character titles
            for (let i = 0; i < 4; i++) {
                for (let j = 0; j < countC; j++) {
                    var tempTitle = (characterArrayTitles[j] + (i + 1));
                    data.Character[0][tempTitle] = characterArray[tempTitle];
                    //console.log(data.CharacterInfo[0][tempTitle]); 
                }
            }

            //set up JSON file
            outputFile = JSON.stringify(data, null, 2);
            //Download the file
            downloadFile("ImageProperties.txt", outputFile)

        })
        .catch(err => console.log(err))


}


function downloadFile(filename, data) {

    //PATH C:/Users/danie/Documents/GitHub/CSC7058/CSC7058WebAppV2/app/static/imageProperties/. Can't select path.
    // Convert the text to BLOB.
    const textToBLOB = new Blob([data], { type: 'text/plain' }); //creates a text file from output file passed in
    //const sFileName = 'formData.txt'; // The file to save the data. 
    let newLink = document.createElement("a"); //creates a document element. Can be called anything. Not placed in DOM.
    newLink.download = filename; //Creates a download link to store file locally. Cannot download directly due to security.
    if (window.webkitURL != null) { //
        newLink.href = window.webkitURL.createObjectURL(textToBLOB);
        newLink.click();
    }
    else {
        newLink.href = window.URL.createObjectURL(textToBLOB);
        newLink.style.display = "none";
        document.body.appendChild(newLink);
        newLink.click();
        document.body.removeChild(newLink);
    }

}



async function downloadImage(downloadImage, downloadName) {
    //download image file that user has selected / rendered
    if (downloadImage != "") {
        imageSrc = downloadImage;
    } else {
        imageSrc = "/static/RenderLibrary/Best_Beaches_Surfing20220313_14-57-54.jpg";
    }

    const image = await fetch(imageSrc)
    const imageBlog = await image.blob()
    const imageURL = URL.createObjectURL(imageBlog)

    const link = document.createElement('a')
    link.href = imageURL
    link.download = downloadName
    document.body.appendChild(link)
    link.click()
    document.body.removeChild(link)

}



