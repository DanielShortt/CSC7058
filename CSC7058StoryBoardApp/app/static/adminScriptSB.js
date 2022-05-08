async function adminTipModal() {
    var myModal = new bootstrap.Modal(document.getElementById('adminTipModal'), {})
    myModal.toggle()   
}
window.onload = adminTipModal;

// function reloadApp(){


//     //temp method to load in JSON. Need to figure out how to modify data loaded in.
//     fetch('static/JSON/labels.json')
//         .then(response => response.json())
//         .then(data => {


//             //Store number of scene properties selected
//             //var count = Object.keys(data.Environment[0]).length;
//             //var keys = Object.keys(data.Environment[0]);
//             var count1 = Object.keys(data.Environment[0]["Time"][0]).length;
//             var keys1 = Object.keys(data.Environment[0]["Time"][0]);
//             //console.log(keys1);
//             //Store number of character properties selected

//             for (let i = 0; i < count1; i++) {
//                 if(data.Environment[0]["Time"][0][keys1[i]] == "Twilight"){
//                     console.log("FOUND")
//                 }


//             }
//             //console.log(count);

            
//         })
//         .catch(err => console.log(err))

// }