// function showOptions() {
  
//     chrome.windows.create(
//         {'url': 'newtab.html', 'type': 'popup'} , function(window) {
//             tabCreatedID = window.tabs[0].id;
//             window.focused = true;
//             //setTimeout(function(){chrome.tabs.remove(window.tabs[0].id);}, 3000)
//         //chrome.runtime.sendMessage({type:'windowsCreated',windowsID:window.tabs[0].id});
   
//         });


//         chrome.tabs.create({
//             url: chrome.extension.getURL('newtab.html'),
//             active: false
//         });
//  };

//  showOptions();

 chrome.runtime.sendMessage({type:'click_security_extension'});


//  var createData = {
//     "url": "https://www.google.com",
//     "type": "popup",
//     "top": 5,
//     "left":5,
// // "width":screen.availWidth/2,
// // "height": screen.availHeight/2
// };
// chrome.windows.create(createData,function(){

// });