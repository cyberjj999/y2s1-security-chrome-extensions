// document.querySelector('.close').addEventListener("click", function() {
// 	document.querySelector('.bg-modal').style.display = "none";
// });

var x = 0;
chrome.runtime.sendMessage({type:'click_extension'});


// chrome.browserAction.setTitle({
//   title:'This is the tooltip text upon mouse hover.'
// });

// var callback = function () {
//     // Do something clever here once data has been removed.
//     alert("Data has been cleared");
//   };
  


//   var r = confirm("Are you sure you want to clear browsing data?!");
//   if (r == true) {
//     var millisecondsPerWeek = 50000;
//   var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
//   chrome.browsingData.remove({
//     "since": oneWeekAgo
//   }, {
//     "appcache": true,
//     "cache": true,
//     "cacheStorage": true,
//     "cookies": true,
//     "downloads": true,
//     "fileSystems": true,
//     "formData": true,
//     "history": true,
//     "indexedDB": true,
//     "localStorage": true,
//     "pluginData": true,
//     "passwords": true,
//     "serviceWorkers": true,
//     "webSQL": true
//   }, callback);
//   } else {
//     txt = "Data has not been cleared";
//   }

// wikiUrl = "options.html";
//   var createData = {
//     "url":wikiUrl,
//     "type": "popup",
//     "top": 5,
//     "left":5,
//     "width":screen.availWidth/2,
//     "height": screen.availHeight/2
// };
// chrome.windows.create(createData,function(){

// });
  
// function showOptions() {
//   var w = 440;
//   var h = 220;
//   var left = (screen.width/2)-(w/2);
//   var top = (screen.height/2)-(h/2); 

//   chrome.windows.create({'url': 'options.html', 'type': 'popup', 'width': w, 'height': h, 'left': left, 'top': top} , function(window) {
//   });
// };

// showOptions();

