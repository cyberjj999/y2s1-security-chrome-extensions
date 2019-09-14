var tabCreatedID = 0;

function showOptions() {
    var w = 460;
    var h = 386;
    var left = (screen.width/2)-(w/2);
    var top = (screen.height/2)-(h/2); 
  
    chrome.windows.create(
        {'url': 'options.html', 'type': 'popup', 'width': w, 'height': h, 'left': left, 'top': top , 'focused': true} , function(window) {
            tabCreatedID = window.tabs[0].id;
            //setTimeout(function(){chrome.tabs.remove(window.tabs[0].id);}, 3000)
        //chrome.runtime.sendMessage({type:'windowsCreated',windowsID:window.tabs[0].id});
   
        });
 };


//vid = null;

// chrome.runtime.onMessage.addListener(function(request) {
//     if (request.type === 'click_extension') {
//         chrome.windows.get(vid, function(chromeWindow) {
//             if (!chrome.runtime.lastError && chromeWindow) {
//                 chrome.windows.update(vid, {focused: true});
//                 return;
//             }

//             showOptions();
//             function X(chromeWindow){
//                 vid = chromeWindow.id;
//             }
//             X();
//         });
//         //showOptions();
//         //vid = chromeWindow.id;
        
//     }
// });

chrome.runtime.onMessage.addListener(function(request) {
    if (request.type === 'click_extension') {
            showOptions();

        }
        //if possible , make it such that they cannot open twice
        //https://stackoverflow.com/questions/9686356/google-chrome-extensions-create-a-window-only-once
        //this may be helpful
});

chrome.runtime.onMessage.addListener(function(request) {
    if (request.type === 'clearedData') {
        chrome.tabs.remove(tabCreatedID);

        }
});

var menuItem = {
    "id": "cleanIt",
    "title": "Clean It!",
    "contexts": ["all"]
};

chrome.contextMenus.create(menuItem);
//Add a listener to do something when user clicks on context menu
    chrome.contextMenus.onClicked.addListener(function(clickData){  
        
        showOptions();  
    
});











/*
chrome.windows.get(vid, function(chromeWindow) {
    if (!chrome.runtime.lastError && chromeWindow) {
        chrome.windows.update(vid, {focused: true});
        return;
    }
    chrome.windows.create(
        {'url': 'my_url', 'type': 'panel', 'focused': true},
        function(chromeWindow) {
            vid = chromeWindow.id;
        }
    );
});*/