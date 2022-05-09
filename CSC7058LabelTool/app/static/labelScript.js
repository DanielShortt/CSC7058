//START OF SCRIPTING FILES

//GLOBAL VARIABLES
var divShown = "";
var charDivShown = "";
var charCount = 0, charTotal = 1;
var outputFile = "";
var clickCount = 0;

const environmentArrayTitles = ["time", "setting", "lighting", "atmosphere", "mainProp", "propLoc", "camera", "numberChars"];
const characterArrayTitles = ['gender', 'charLoc','hair', 'pose', 'top', 'bottoms', 'prop'];
                            
const environmentArray = { 'time': '', 'setting': '', 'lighting': '', 'atmosphere': '', 'mainProp': "", 'propLoc': '', 'camera': '', 'numberChars': '' };

const characterArray = {
    'gender1': '', 'charLoc1': '','hair1': '', 'pose1': '', 'top1': '', 'bottoms1': '', 'prop1': '',
    'gender2': '', 'charLoc2': '','hair2': '', 'pose2': '', 'top2': '', 'bottoms2': '', 'prop2': '',
    'gender3': '', 'charLoc3': '','hair3': '', 'pose3': '', 'top3': '', 'bottoms3': '', 'prop3': '',
    'gender4': '', 'charLoc4': '','hair4': '', 'pose4': '', 'top4': '', 'bottoms4': '', 'prop4': ''
};
//End of array

//FUNCTION TO HIDE DIV
function divHide(id, cara) {
    //Take ID of hair selected and add to Json file in background.
    buttonid = id
    var T = document.getElementById(cara);
    T.style.display = "none";  // <-- Set it to block
    divShown = "";
}

//FUNCTION TO HIDE CHARACTER CREATION DIV
function hideCharDiv(id, cara) {
    //Take ID of hair selected and add to Json file in background.
    buttonid = id
    var T = document.getElementById(cara);
    T.style.display = "none";  // <-- Set it to block
    charDivShown = "";
}

//FUNCTION TO SHOW DIV
function showDiv(divId, element) {
    if (divShown != "") {
        divHide("", divShown);
    }
    document.getElementById(divId).style.display = 'block';
    divShown = divId;
}

//FUNCTION TO SHOW CHRACTER CREATION DIVS
function showCharDiv(divId, element) {
    if (charDivShown != "") {
        hideCharDiv("", charDivShown);
    }

    document.getElementById(divId).style.display = 'block';
    charDivShown = divId;
}

//FUNCTION TO SET NUMBER OF CHARS SELECTED TO CONTROL LOOP 
//FUNCTION SETS UP DIVS FOR SETTING CHRACTER CREATION VARIABLES
function charInfo(numOfChars) {
    //Add Char info here. Must take int argument to control loop iterations.

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
        var charLoopTitle = "Character " + charCount;
        CharLoopTitleId = "charNumTitle"
        var updateCharLoopTitle = document.getElementById(CharLoopTitleId);
        updateCharLoopTitle.innerHTML = charLoopTitle;
        var charIdUpdate = "caraCharDetails" + charCount;
        var updateCharLoopId = document.getElementById("caraCharDetails").id;
        document.getElementById("caraCharDetails").id = charIdUpdate;
        document.getElementById(charIdUpdate).style.display = 'block';
    } else if(charTotal = 0){
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


    } else {
        //update property already selected to new value selected by user
        document.getElementById(objectLabelId).innerHTML = object;

        elementExists = false;
    }
}


//Create the character Labels and store them in global variables above
//labels stored in labels column under character header   
function addCharElement(object, label) {

    //high level variables required for function
    var temp = "";
    var elementExists = false;
    var objectLabelId = "";
    var objectLabelId = "";
    var newCharDiv = "";
    var elementExists = false, charExists = false;
    var charClassTitle = "charLabels" + charCount; //should always start at if char number selected is greater than 1

    //Create new High level character label divs
    if (document.getElementById(charClassTitle)) {
        charExists = true
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

        const currentDiv = document.getElementById("charLabels" + (charCount - 1));
        const parentDiv = document.getElementById("charObjects");
        parentDiv.insertBefore(newCharDiv, currentDiv.nextSibling);
    }

    if (charCount > 0) {
        temp = label + charCount  //eg gender1
    }

    var item = characterArray[temp];

    if (item != '') {
        elementExists = true;
    }

    //Looking  in character array and storing value for label + current active character number
    characterArray[temp] = object;
    objectLabelId = temp + "id";
    var currentCharDiv = "";

    //if element does not exist create a new element and popluate active character
    if (elementExists == false) {

        //console.log("About to create a new Character element");

        // create a new div element
        const newDiv = document.createElement("div");
        newDiv.className = "row aCharacterObject" + charCount;
        newDiv.id = "aCharacterObject" + charCount;
        newDiv.style.display = "block";
        newDiv.setAttribute("onclick", "showDiv('caraNumChars',1), activeChar(this.id),showCharDiv('" + label + "')"); //activeChar(id)

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

        // add the newly created element and its content into the DOM
        const currentDiv = document.getElementById("charLabels" + charCount).appendChild(newDiv);

    } else { // else update element that already exists with new selection
        document.getElementById(objectLabelId).innerHTML = object;

        elementExists = false;
    }
}


//CODE to show/hide active and inactive char creation.
function activeChar(id) {

    var activeChar1 = document.getElementsByClassName("aCharacterObject1");
    var activeChar2 = document.getElementsByClassName("aCharacterObject2");
    var activeChar3 = document.getElementsByClassName("aCharacterObject3");
    var activeChar4 = document.getElementsByClassName("aCharacterObject4");

    for (let i = 0; i < activeChar1.length; i++) {

        if (id == "characterLabelHeader1" || id == "aCharacterObject1") {
            updateCurrentChar(1);
            activeChar1[i].style.display = "block";
        } else {
            activeChar1[i].style.display = "none";
        }

    }

    for (let i = 0; i < activeChar2.length; i++) {
        if (id == "characterLabelHeader2" || id == "aCharacterObject2") {
            updateCurrentChar(2);
            activeChar2[i].style.display = "block";
        } else {
            activeChar2[i].style.display = "none";
        }
    }

    for (let i = 0; i < activeChar3.length; i++) {
        if (id == "characterLabelHeader3" || id == "aCharacterObject3") {
            updateCurrentChar(3);
            activeChar3[i].style.display = "block";
        } else {
            activeChar3[i].style.display = "none";
        }
    }

    for (let i = 0; i < activeChar4.length; i++) {
        if (id == "characterLabelHeader4" || id == "aCharacterObject4") {
            updateCurrentChar(4);
            activeChar4[i].style.display = "block";
        } else {
            activeChar4[i].style.display = "none";
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


function loginModal() {
    var myModal = new bootstrap.Modal(document.getElementById('labelLoginModal'), {})
    myModal.toggle()   
}



