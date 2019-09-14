// function urlify(text) {
//     var urlRegex = /(https?:\/\/[^\s]+)/g;
//     return text.replace(urlRegex, function(url) {
//         return '<a href="' + url + '">' + url + '</a>';
//     })
//     // or alternatively
//     // return text.replace(urlRegex, '<a href="$1">$1</a>')
// }

// var text = "Find me at http://www.example.com and also at http://stackoverflow.com";
// var html = urlify(text);

// html now looks like:
// "Find me at <a href="http://www.example.com">http://www.example.com</a> and also at <a href="http://stackoverflow.com">http://stackoverflow.com</a>"


// function do_ajax(urlParameter) {
//     var req = new XMLHttpRequest();

//     req.onreadystatechange = function()
//     {
//       if(this.readyState == 4 && this.status == 200) {
//         var smth ="hello";
//       } else {
//         var smth ="not hello";
//       }
//     }
// req.open('POST', 'http://192.168.1.105:5000', true);
// //req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
// req.send(urlParameter);
// }

var tabUpdated = false;


// chrome.webNavigation.onHistoryStateUpdated.addListener(function (){
//   alert("Onhistoryupdate")
// })


 //, {url: [{urlMatches : 'https://*/'}]});

 
      // chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab){
      //   //if (changeInfo.status == 'complete' && tab.status == 'complete' && tab.url != undefined) {
      //       if (!tabUpdated) {
      //           alert("tab load complete");
      //           tabUpdated = true;
      //       }
      //  // }
      // });
//webNavigation.onCompleted -> Keeps firing nonstop
//Can try use storage API for this thingy
//tabs.onUpdated -> Don't work when theres cache (old document wont load)
//webNavigation.onTabReplaced -> Only fired at prerendered tab (new doucment wont load)

// chrome.webRequest.onBeforeRequest.addListener(function(details){
 
//   chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
//     //alert("This ran");

//     //Im so damn smart here bruh
//     //This set it such that if the URL is the same,  it wont run again
//     //but everytime u go into another URL , it will run once
//     //took me fuckin hours to do smth like this , api research aint do shit
//     //this is pure INTELLECT RIGHT HERE BOIIIIIIIIIIIIIIIIIII
//      if (urlTested != tab.url){

//         alert("This will run once per website");
//           $.ajax({
//         type: "POST",
//         url: "http://192.168.1.105:5000", //home wifi
//         //url: "http://172.27.176.152:5000", //school wifi
//         contentType: "application/json",
//         //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
//         //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
//         data: JSON.stringify({URLText: tab.url}),
//         //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}
//         dataType: "json",
//         success: function(response) {
//             //alert("Successfully sent");
//             //alert(JSON.stringify(response));
//             if(response == "Good"){

//                 alert("Its actually good")
//             }
            
//             else if (response == "There is a problem"){
//                 alert("The response received is " + JSON.stringify(response));
                
//             }
//             else {
//               alert("The response received is " + JSON.stringify(response));
//               alert("Warning! Malicious URL detected!")
//                 //document.body.style.display='none';
//             }
//             //console.log(response);
//         },
//         error: function(err) {
//             alert("Fail to get a response");
//             //console.log(err);
//         }
//     });
//       urlTested = tab.url;
//      }


    
//   });
 
  
// },
// {urls: ["<all_urls>"],
// types:['main_frame']})



// function queryServer(){
//   $.ajax({
//     async: false,
//     type: "POST",
//     url: "http://192.168.1.105:5000", //home wifi
//     //url: "http://172.27.180.228:5000", //school wifi
//     contentType: "application/json",
//     //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
//     //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
//     data: JSON.stringify({URLText: stringURL}),
//     //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}
//     dataType: "json",
//     success: function(response) {
//         //alert("Successfully sent");
//         //alert(JSON.stringify(response));
//         if(response == "Good"){
//             //alert(JSON.stringify(response));
//             //alert("Its actually good")
//             myFunction();
//         }
        
//         else {
//           //alert("The response received is " + JSON.stringify(response));
//           //alert("Warning! Malicious URL detected!")
//           myFunction();
//             //document.body.style.display='none';
//         }
//         //console.log(response);
//     },
//     error: function(err) {
//         alert("Fail to get a response");
//         //console.log(err);
//     }
// });
// }



// var urlTested = "";
// chrome.webRequest.onBeforeRequest.addListener(function(details){
 
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
//     //alert("This ran");
//     var tab = tabs[0];
//     var stringURL = tab.url;
//     //Im so damn smart here bruh
//     //This set it such that if the URL is the same,  it wont run again
//     //but everytime u go into another URL , it will run once
//     //took me fuckin hours to do smth like this , api research aint do shit
//     //this is pure INTELLECT RIGHT HERE BOIIIIIIIIIIIIIIIIIII
//      if (urlTested != stringURL){
//        //queryServer();
//         //alert("This will run once per website");
//           $.ajax({
//         type: "POST",
//         url: "http://192.168.1.105:5000", //home wifi
//         //url: "http://172.27.180.228:5000", //school wifi
//         contentType: "application/json",
//         //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
//         //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
//         data: JSON.stringify({URLText: stringURL}),
//         //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}
//         dataType: "json",
//         success: function(response) {
//             //alert("Successfully sent");
//             //alert(JSON.stringify(response));
//             if(response == "Good"){
//                 //alert(JSON.stringify(response));
//                 //alert("Its actually good")
//                 myFunction();
//             }
            
//             else {
//               //alert("The response received is " + JSON.stringify(response));
//               //alert("Warning! Malicious URL detected!")
//               myFunction();
//                 //document.body.style.display='none';
//             }
//             //console.log(response);
//         },
//         error: function(err) {
//             alert("Fail to get a response");
//             //console.log(err);
//         }
//     });
//       urlTested = tab.url;
//      }

     


    
//   });
 
//   return {cancel: true};},
// {urls: ["<all_urls>"],
// types:['main_frame']})



// chrome.webRequest.onBeforeRequest.addListener(function(){

//     chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
         
//     var tab = tabs[0];
      
//     var url = new URL(tab.url);
    
//     var smth = tab.url;
//     if(url == smth){
//     //alert(smth);
//     }
//     else {
//       //alert("No");
//     }
//     });
//   //alert("This runs before you NAVIGATE");
// })
// chrome.webNavigation.onBeforeNavigate.addListener(function(){
//   chrome.tabs.onUpdated.addListener(function (tabId, changeInfo, tab) {
        
//     if(changeInfo.status == 'complete'){
//       //myFunction();
//       //alert("This ran");
//         var X = tab[0];
//         var url = new URL(tab.url);
//         var testURL = tab.url;
        
// // $.ajax({
// //   type: "POST",
// //   //url: "http://192.168.1.105:5000", //home wifi
// //   url: "http://172.27.181.72:5000", //school wifi
// //   contentType: "application/json",
// //   //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
// //   //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
// //   data: JSON.stringify({URLText: "https://www.google.com"}),
// //   //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}
// //   dataType: "json",
// //   success: function(response) {
// //       alert("Successfully sent");
// //       alert(JSON.stringify(response));
// //       if(response == "Good"){
// //           //alert("Do nothing here")
// //       }
// //       else {
// //           myFunction();
// //           //alert("Warning! Malicious URL detected!")
          
// //       }
// //       //console.log(response);
// //   },
// //   error: function(err) {
// //       alert("Fail to get a response");
// //       //console.log(err);
// //   }
// // });
//     }
//             });

// });

// var blockedURLs = function(){
  
//   return ["*//www.evil.com/*"];
// }




// chrome.webRequest.onBeforeRequest.addListener(function() { 
  
//     var num1 = 4;
//     alert(num1);
//     alert("smth");
//     alert("smth2");
      
//       return {cancel: true}; },
//   {urls: ["<all_urls>"]});

// var urlTested = "";

//     chrome.webRequest.onBeforeRequest.addListener(function(info) {
//         chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
          
//           var tab = tabs[0];
//           var stringURL = tab.url;
//           //Im so damn smart here bruh
//           //This set it such that if the URL is the same,  it wont run again
//           //but everytime u go into another URL , it will run once
//           //took me fuckin hours to do smth like this , api research aint do shit
//           //this is pure INTELLECT RIGHT HERE BOIIIIIIIIIIIIIIIIIII
//         if (urlTested != stringURL){
//           urlTested = stringURL;
          

//            $.ajax({
//         type: "POST",
//         url: "http://192.168.1.105:5000", //home wifi
//         //url: "http://172.27.180.228:5000", //school wifi
//         contentType: "application/json",
//         data: JSON.stringify({URLText: stringURL}),
//         dataType: "json",
//         success: function(response) {
//             //alert("Successfully sent");
//             //alert(JSON.stringify(response));
//             if(response == "Good"){
//                 //alert(JSON.stringify(response));
//                 myFunction();

//             }
//             else if(response == "No such website"){
//               alert("Invalid website");
//             }
//             else {
//               //alert("The response received is " + JSON.stringify(response));
//               //alert("Warning! Malicious URL detected!")
//               myFunction();
//                 //document.body.style.display='none';
//             }
//             //console.log(response);
//         },
//         error: function(err) {
//             alert("Fail to get a response");
//             //console.log(err);
//         }
//     });

//      }
//       else {

//       }
       
//             });
           
//       },
//       // filters
//       {
//         urls: [
//           "http://*/",
//           "https://*/*",
//           "<all_urls>"



//         ]
        
//       },
//       // extraInfoSpec
//       ["blocking"]);

      
// chrome.webRequest.onBeforeRequest.addListener(function() { 
  
//     var num1 = 4;
//     alert(num1);
//     alert("smth");
//     alert("smth2");
      
//       return {cancel: true}; },
//   {urls: ["<all_urls>"]});

// function sendFalsePositiveReport(goodURL){
//   $.ajax({
//     type: "POST",
//     //url: "http://192.168.1.105:5000/hello", //home wifi
//     url: "http://172.27.181.142:5000", //school wifi
//     contentType: "application/json",
//     data: JSON.stringify({URLText: goodURL}),
//     dataType: "json",
//     success: function(response) {
//        //alert(JSON.stringify(response));
        
//     },
//     error: function(err) {
//         alert("Fail to get a response");
//     }
//   });
// }

chrome.storage.sync.get(['dndList'],function(data){
  if (typeof data.dndList === "undefined") {

      //alert("dndList is empty");
      var dndArray = ["https://www.google.com/"];
      chrome.storage.sync.set({'dndList': dndArray});
  }
  else {
      //alert("dndList is not empty");

  }

  })

function myFunction(maliciousURL) {
  
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
      chrome.tabs.update(null,{url:"blockpage.html"},function(){
        chrome.storage.sync.set({'currentMaliciousList': maliciousURL});
      });

    });

}

function checkURL(stringURL){
  chrome.storage.sync.get(['dndList','currentMaliciousList'],function(data){
    // alert("my dnd list includes " + data.dndList);
    // alert("my stringURL is " + stringURL);
    // alert(data.dndList.includes(stringURL));
  if (stringURL == data.currentMaliciousList){
    //alert("not sending cus its inside my currentMaliciousList")
  }

  else if(data.dndList.includes(stringURL)){
    //LOOP THROUGH , U CANNOT DO LIKE THIS
    //ONE FALSE ISIT ALL FALSE?
    //alert("im not checking blackboard")
  }
 
  else {
  $.ajax({
            type: "POST",
            //url: "http://192.168.1.105:5000", //home wifi
            //url: "http://172.27.181.142:5000", //school wifi
            url: "http://192.168.43.55:5000", //hotspot
            contentType: "application/json",
            data: JSON.stringify({URLText: stringURL}),
            dataType: "json",
            success: function(response) {
                //alert("Successfully sent");
                //alert(JSON.stringify(response));
                if(response == "Good"){
                    //alert(JSON.stringify(response));
                    //myFunction();
                    //alert("Website is good");
                    //myFunction(stringURL);

                } 
                else if(response == "No such website"){
                  //alert("Website do not exists");
                  //alert("Invalid website");
                }
                else {
                  //alert("The response received is " + JSON.stringify(response));
                  //alert("Warning! Malicious URL detected!")
                  myFunction(stringURL);
                    //document.body.style.display='none';
                }
                //console.log(response);
            },
            error: function(err) {
                //alert("Fail to get a response");
                //myFunction(stringURL);

                //console.log(err);
            }
        });
      }

      });
 
}



// //Uncomment this - ORIGINAL ALGORITHM TO TEST
// var urlTested = "";
// var stringURL = '';
//     chrome.webRequest.onBeforeRequest.addListener(function(info) {

//         chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
//               var tab = tabs[0];
//               stringURL = tab.url;
          
//             if (urlTested != stringURL){
//               urlTested = stringURL;
              

//            $.ajax({
//         type: "POST",
//         //url: "http://192.168.1.105:5000", //home wifi
//         url: "http://172.27.181.78:5000", //school wifi
//         contentType: "application/json",
//         data: JSON.stringify({URLText: stringURL}),
//         dataType: "json",
//         success: function(response) {
//             //alert("Successfully sent");
//             //alert(JSON.stringify(response));
//             if(response == "Good"){
//                 //alert(JSON.stringify(response));
//                 //myFunction();
//                 alert("Website is good");

//             } 
//             else if(response == "No such website"){
//               alert("Website do not exists");
//               //alert("Invalid website");
//             }
//             else {
//               //alert("The response received is " + JSON.stringify(response));
//               //alert("Warning! Malicious URL detected!")
//               myFunction();
//                 //document.body.style.display='none';
//             }
//             //console.log(response);
//         },
//         error: function(err) {
//             alert("Fail to get a response");
//             //console.log(err);
//         }
//     });

//      }
//       else {

//       }
       
         

//         });
 
           
//       },
//       // filters
//       {
//         urls: [
//           "http://*/",
//           "https://*/*",
//           "<all_urls>"



//         ]
        
//       },
//       // extraInfoSpec
//       ["blocking"]);


//         chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
//               var tab = tabs[0];
//               stringURL = tab.url;
          
//             if (urlTested != stringURL){
//               urlTested = stringURL;
//            }
//            else {
//    }   
          
//             })
//              
                            
// function runningFunction(){
//   chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
//     var tab = tabs[0];
//     stringURL = tab.url;

//     //assume it is good first
    
//   if (urlTested != stringURL){

//     urlTested = stringURL;

//     checkURL();
//     //This lines of algorithm SHOULD RUN before user can even navigate to the webpage
//     var xx = 10;
//     var p = 5+10;
    
//     alert("p value is " + p);
    
//     //Act as tho this is the algo you run , if not malicious , do nothing
//     if (p==14){
//       //if good do nth
//     }
//     else {
//       //if bad redirect to blockpage.html
//     return {cancel:true}; 
//     } 
//   }

//   //Duplicate event ,dont do anth here , if not will keep looping
//   else {
  
//   }   

//   });

// }


// var urlTested = "";
// // var stringURL = ''; 
// chrome.webRequest.onBeforeRequest.addListener(function(details) {
//   //runningFunction();
 
// }

 
// ,

//   {urls: ["http://*/",
//   "https://*/*",
//   "<all_urls>"]
//     },

//   ["blocking"]);



// var a = ''
// $('a').mousedown(function(){
//     alert($(this).attr('href'));
// });



//This may work but not a v good idea..?
//Gmail actually show the content , so it doesnt really stop at the buffer stage ,i believe bc
//of the delay in sending of messages , they got loaded 1 more step
// chrome.webRequest.onBeforeRequest.addListener(function(details) {
//   chrome.runtime.onMessage.addListener(function(request) {
//   if (request.navigation === 'true') {
//         //alert("my request url is " + request.url);
//         checkURL(request.url);
//       }

// });

chrome.webRequest.onBeforeRequest.addListener(function(details){
      chrome.tabs.query({ active: true, currentWindow: true }, function (tabs,changeInfo) {
         
    var tab = tabs[0];
      
    var url = new URL(tab.url);
    url = String(url);
  //alert("it has ran");
    checkURL(url); 

      });
},
{urls: ["<all_urls>"],
types:['main_frame']})