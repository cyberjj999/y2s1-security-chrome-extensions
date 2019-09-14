var Query = {
    "id": "query",
    "title": "Stop news query",
    "contexts": ["all"]

};

function showOptions() {
  
    chrome.windows.create(
        {'url': 'newtab2.html', 'type': 'popup'} , function(window) {
            tabCreatedID = window.tabs[0].id;
            window.focused = true;
            //setTimeout(function(){chrome.tabs.remove(window.tabs[0].id);}, 3000)
        //chrome.runtime.sendMessage({type:'windowsCreated',windowsID:window.tabs[0].id});
   
        });


        // chrome.tabs.create({
        //     url: chrome.extension.getURL('newtab.html'),
        //     active: false
        // });
 };

 chrome.runtime.onMessage.addListener(function(request) {
    if (request.type === 'click_security_extension') {
            showOptions();

        }
        //if possible , make it such that they cannot open twice
        //https://stackoverflow.com/questions/9686356/google-chrome-extensions-create-a-window-only-once
        //this may be helpful
});

//alert("Starting to query");
chrome.contextMenus.create(Query);
// chrome.storage.sync.set({'Query': "True"});

chrome.storage.sync.get(['Query'], function(result) {
    //alert("Result.query is " + result.Query);
    //alert(typeof(result.Query));
    //is string lmao
    if (typeof result.Query === "undefined") {

        chrome.storage.sync.set({'Query': "True"});
        //alert("result.query should not be equal to true or false");

    }
});

//IF current is true , when u click , u want it to become false
chrome.contextMenus.onClicked.addListener(function(clickData){     
            chrome.storage.sync.get(['Query'], function(result) {
        if (result.Query == 'True') {
            chrome.contextMenus.update("query",{
                "title": "Start news query",
                "contexts": ["all"],
                        });
            chrome.storage.sync.set({'Query': "False"});
            alert("Query has been deactivated");

        }
        else if (result.Query == 'False'){
            chrome.contextMenus.update("query",{
                "title": "Stop news query",
                "contexts": ["all"],
                        });
            chrome.storage.sync.set({'Query': "True"});
           alert("Query has been activated");

            }
                        
                });
    });










// });


// chrome.storage.sync.get(['Query'], function(result) {
//         if (result.Query == 'False') {
//             chrome.contextMenus.create(startQuery);
//             //Add a listener to do something when user clicks on context menu
//                 chrome.contextMenus.onClicked.addListener(function(clickData){  
                    
//                     chrome.storage.sync.set({Query: "True"}, function() {
//                       });
                    
                
//             });
//         }
//         else {
//         chrome.contextMenus.create(stopQuery);
//         chrome.contextMenus.onClicked.addListener(function(clickData){     
//         chrome.storage.sync.set({Query: "False"}, function() {
//                  });

//                  alert("okay , ill set it to false");

//                  chrome.storage.sync.get(['Query'], function(result) {
//                     if (result.Query == 'False') {
//                             alert("ayy i got false");
//                             }
//                         });
//             });
//         }

//   });
// var outcome = 0;
//   function checkQueryStatus(){
//     chrome.storage.sync.get(['Query'], function(result) {
//         if (result.Query == 'False') {
//             outcome = 1;
//             /*
//             chrome.storage.sync.get(['total','limit'], function(budget){
//                     var newTotal = 0;
//                     if (budget.total){
//                         newTotal += parseInt(budget.total);
//                     }
    
//                     newTotal += parseInt(clickData.selectionText);
//                     chrome.storage.sync.set({'total': newTotal}, function(){   
//             */
//         }
//         else {
//             outcome = 2;
//         }

//     });
//     return outcome;

//   }



// alert(checkQueryStatus());
