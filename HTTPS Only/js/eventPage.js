function checkWebsite(urlToCheck){

  $.ajax({
    type: "HEAD",
    url: urlToCheck,
    success: function(msg){
      var opt = {
        type: 'basic',
        title: 'We detected a usage of HTTP unsecure protocol!',
        message: 'Changing http protocol to https ...',
        iconUrl:"icon/HTTPS16.png"
        };
        
        chrome.notifications.create(opt);
        chrome.tabs.update(null,{url:urlToCheck});
      
    },
    error: function(err) {
          //No https version
   }
  }
)};

// chrome.storage.sync.get(['httpChecked'],function(data){
//   //alert('My current status is ' + data.httpChecked);
//   //It will always start off as undefined when u re-load the extension
//   if (typeof data.httpChecked === "undefined") {
//       var checkedStatus = "No";
//       chrome.storage.sync.set({'httpChecked': checkedStatus});
//   }
//   else if (data.httpChecked == 'Yes') {
//       //alert("HTTPS only");
//   }

//   else {
//     //alert("HTTP and HTTPS");
//   }

//   });


chrome.runtime.onMessage.addListener(function(request) {
  if (request.httpNavigation === 'true') {
    chrome.storage.sync.get(['httpChecked'],function(data){
    //alert('My current status is ' + data.httpChecked);
    //It will always start off as undefined when u re-load the extension
    if (typeof data.httpChecked === "undefined") {
        var checkedStatus = "No";
        chrome.storage.sync.set({'httpChecked': checkedStatus});
    }
    else if (data.httpChecked == 'Yes') {
        //alert("HTTPS only");
         chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var tab = tabs[0];
        var urlString = new URL(tab.url);
        //alert("my urlstring is " + urlString);

        urlString.protocol = 'https';
        //alert("my urlstring now is " + urlString);
        urlString = String(urlString);
        chrome.tabs.update(null,{url:urlString});

        });
    }

    else {
      //alert("HTTP and HTTPS");
        chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        var tab = tabs[0];
        var urlString = new URL(tab.url);
        //alert("my urlstring is " + urlString);

        urlString.protocol = 'https';
        //alert("my urlstring now is " + urlString);
        urlString = String(urlString);
        checkWebsite(urlString);
        });
    }

    });

  
      }
});


// var urlName = ''
// //var smth = ''

//  chrome.webNavigation.onDOMContentLoaded.addListener(function(){
        
//         chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
          
//             //var tab = tabs[0];
//             //alert("TAB IS " + tab)

//             var tab = tabs[0];
//             var url = new URL(tab.url);
//             smth = tab.url;
//             //var smth = tabs.url;

//             //alert(smth);
//             //alert(urlName);
//             if(urlName == smth){

//             }
//             else{

//               try {
//               var req = new XMLHttpRequest();
//               var urlToReload = smth.replace("http","https");
        

//               //req.getResponseHeader('Header')
//               req.open('GET', urlToReload, false);
              
//               req.send(null);
//               //var urlToReload = smth.replace("http","https");
//               var opt = {
//               type: 'basic',
//               title: 'We detected a usage of HTTP unsecure protocol!',
//               message: 'Changing http protocol to https ...',
//               iconUrl:"HTTPS16.png"
//               };

//               chrome.notifications.create(opt);
//               chrome.tabs.update(null,{url:urlToReload});
//               urlName = smth;
//               }
//               catch(e){
                  
//               }
                
//             }
             
          
//           });


//           //alert(smth);

//           } , {url: [{urlMatches : 'http://*'}]});





// chrome.webRequest.onBeforeRequest.addListener(function(details){
 
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {

// });
 
//   return {cancel: true};},
// {urls: ["<all_urls>"],

// chrome.webRequest.onBeforeRequest.addListener(function(details){
 
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {

                      
//                 var tab = tabs[0];
//                 var url = new URL(tab.url);
//                 var smth = tab.url;
//                 if(urlName == smth){
    
//                 }
//                 else{
    
//                 try {
//                   var req = new XMLHttpRequest();
//                   var urlToReload = smth.replace("http","https");
    
//                   //req.getResponseHeader('Header')
//                   req.open('GET', urlToReload, false);
//                   req.send(null);
//                   //var urlToReload = smth.replace("http","https");
    
//                   var opt = {
//                   type: 'basic',
//                   title: 'We detected a usage of HTTP unsecure protocol!',
//                   message: 'Changing http protocol to https ...',
//                   iconUrl:"HTTPS16.png"
//                   };
    
//                   chrome.notifications.create(opt);
//                   chrome.tabs.update(null,{url:urlToReload});
//                   urlName = smth;
//                   }
//                   catch(e){
                      
//                   }
                    
//                 }
                 
              
//               });
 
//   return {cancel: true};},
// {urls: ["http://*/"]});