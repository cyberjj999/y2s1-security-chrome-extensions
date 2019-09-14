
// // var anchorme = require("anchorme").default; // if installed via NPM
// // import anchorme from "anchorme"; // ES6 / Typescript style imports
// // var someText = "this is a text with a link www.github.com ..";
// // var result = anchorme(someText)

// // function urlify(text) {
// //     var urlRegex = /(https?:\/\/[^\s]+)/g;
// //     return text.replace(urlRegex, function(url) {
// //         return '<a href="' + url + '">' + url + '</a>';
// //     })
// //     // or alternatively
// //     // return text.replace(urlRegex, '<a href="$1">$1</a>')
// // }

// // var text = "Find me at http://www.example.com and also at http://stackoverflow.com";
// // var html = urlify(text);
// // alert(html);

// // html now looks like:
// // "Find me at <a href="http://www.example.com">http://www.example.com</a> and also at <a href="http://stackoverflow.com">http://stackoverflow.com</a>"

// //URL,URL_LENGTH,NUMBER_SPECIAL_CHARACTERS,CHARSET,SERVER,CONTENT_LENGTH,WHOIS_COUNTRY,WHOIS_STATEPRO,WHOIS_REGDATE,WHOIS_UPDATED_DATE,TCP_CONVERSATION_EXCHANGE,DIST_REMOTE_TCP_PORT,REMOTE_IPS,APP_BYTES,SOURCE_APP_PACKETS,REMOTE_APP_PACKETS,SOURCE_APP_BYTES,REMOTE_APP_BYTES,APP_PACKETS,DNS_QUERY_TIMES,Type
// //B0_911,16,6,us-ascii,Microsoft-HTTPAPI/2.0,324,None,None,None,None,0,0,0,0,0,0,0,0,0,0,0

// /* HERE
// var testURL = "http://www.test.com";
// // URL: it is the anonimous identification of the URL analyzed in the study
// // URL_LENGTH: it is the number of characters in the URL
//     URL_LENGTH = testURL.length;
// // NUMBER_SPECIAL_CHARACTERS: it is number of special characters identified in the URL, such as, “/”, “%”, “#”, “&”, “. “, “=”
// var format = /[ !@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/;
//    var j = 0;
//     for (var i = 0; i < testURL.length; i++) {
//         if(format.test(testURL.charAt(i))){
//             j++;
//         };

//       }
//       NUMBER_SPECIAL_CHARACTERS = j;
//      // alert(j);   

// // CHARSET: it is a categorical value and its meaning is the character encoding standard (also called character set).
//       alert(document.characterSet);
//       //this will work granted u are actually on that website ah
//       loadJSON("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_C0fHXMVHPFuUesgev3ccffRf7okNS&domainName=google.com",gotData);
//       function gotData(data){
//           alert(data);
//       }

// // alert(anchorme.validate.ip("1.1.1.1:3000/something"));
// // // returns true
// // anchorme.validate.ip("1.1.1.500:3000/something");
// // // returns false
// // anchorme.validate.email("alex@array.com");
// // // returns true
// // anchorme.validate.url("google.co.uk");
// // // returns true

// // var someText = "this is a text with a link www.github.com ..";
// // var result = anchorme(someText);
// // alert(result);


// var apiUrl = "https://www.whoisxmlapi.com/whoisserver/WhoisService";
// // Fill in your details
// var username = "Your whois api username";
// var password = "Your whois api password";
// var domain = "google.com";
// var format = "JSON";
// var jsonCallback = "LoadJSON";

// window.addEventListener("load", onPageLoad, false);

// function onPageLoad() {
//     // Use a JSON resource
//     var url = apiUrl
//             + "?domainName=" + encodeURIComponent(domain)
//             + "&username=" + encodeURIComponent(username)
//             + "&password=" + encodeURIComponent(password)
//             + "&outputFormat=" + encodeURIComponent(format);

//     // Dynamically Add a script to get our JSON data from a different
//     // server, avoiding cross origin problems.

//     var head = document.getElementsByTagName("head")[0];
//     var script = document.createElement("script");
//     script.type = "text/javascript";

//     // The function specified in jsonCallback will be called with a
//     // single argument representing the JSON object.

//     script.src = url + "&callback=" + jsonCallback;

//     head.appendChild(script);
// }

// // Do something with the json result we get back
// function LoadJSON(result) {
//     // Print out a nice informative string
//     document.body.innerHTML += "<div>JSON:</div>"
//                             +  RecursivePrettyPrint(result);
// }

// function RecursivePrettyPrint(obj) {
//     var str = "";
//     for (var x in obj) {
//         if (obj.hasOwnProperty(x)) {
//             str += '<div style="'
//                 +  "margin-left: 25px;border-left:1px solid black"
//                 +  '">' + x + ": ";
//             if (typeof(obj[x]) == "string")
//                 str += obj[x];
//             else
//                 str += RecursivePrettyPrint(obj[x]);
//             str += "</div>";
//         }
//     }

//     return str;
// }
// */





// //creates an XMLHttpRequest object:
// // alert("this run");
// // function do_ajax() {
// //     var req = new XMLHttpRequest();

// //     req.onreadystatechange = function()
// //     {
// //       if(this.readyState == 4 && this.status == 200) {
// //         var smth ="hello";
// //       } else {
// //         var smth ="not hello";
// //       }
// //     }
// // req.open('POST', 'http://192.168.1.105:5000', true);
// // //req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
// // req.send("name=bob");
// // }
// // do_ajax();s

// //To find out content length of the header , can find stuff like server also
// // var xhr = $.ajax({
// //     type: "HEAD",
// //     url: "https://www.yahoo.com",
// //     success: function(msg){
// //       alert(xhr.getResponseHeader('Content-Length') + ' bytes');
// //       var contentlength = xhr.getResponseHeader;
// //     }
// //   });

// var blockedURLs = ["http://www.evil.com/*"];

// function myFunction() {
//     var txt;
//     var r = confirm("Warning , Malicious Link Detected with an accuracy of 0.95 , do you still want to continue?!");
//     if (r == true) {
      
      
//     } else {
//       txt = "You pressed Cancel!";
//       chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//         chrome.tabs.update(null,{url:"file:///E:/Year%202%20Sem%201/Network%20Security%20&%20Project/Project/Chrome%20Extensions/Security%20Extensions/Web%20Filtering/blockpage.html"});
  
//       });
//     }

// }

// $.ajax({
//     type: "POST",
//     url: "http://192.168.1.105:5000", //home wifi
//     //url: "http://172.27.176.152:5000", //school wifi
//     contentType: "application/json",
//     //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
//     //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
//     data: JSON.stringify({URLText: "https://www.google.com"}),
//     //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}
//     dataType: "json",
//     success: function(response) {
//         alert("Successfully sent");
//         alert(JSON.stringify(response));
//         if(response == "Good"){
//             //alert("Do nothing here")
//         }
//         else {
//             myFunction();
//             //alert("Warning! Malicious URL detected!")
//             blockedURLs.push("https://www.google.com/*");
//             chrome.webRequest.onBeforeRequest.addListener(
//             function(details) {

//                 chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
//                     chrome.tabs.update(null,{url:"file:///E:/Year%202%20Sem%201/Network%20Security%20&%20Project/Project/Chrome%20Extensions/Security%20Extensions/Web%20Filtering/blockpage.html"});
              
//                   });
//                  return {cancel: true}; 
//                 },
//             {urls: blockedURLs},
//             ["blocking"]
//             );
         
//         }
//         //console.log(response);
//     },
//     error: function(err) {
//         alert("Fail to get a response");
//         //console.log(err);
//     }
// });

// // $.ajax({
// //     type: "POST",
// //     url: "http://alas.common.cddc19.ctf.sg/login",
// //     contentType: "application/json",
// //     data: JSON.stringify({username: "test"}),
// //     dataType: "json",
// //     success: function(response) {
// //         alert("successfuly bruh");
// //         alert(JSON.stringify(response));
// //         console.log(response);
// //     },
// //     error: function(err) {
// //         alert("did not work bruh");
// //         console.log(err);
// //     }
// // });

// // const API_URL = '/api'
// // const input = "This is whawt i sent";

// // const handleResponse = ({ target }) => {
// //     // Do something useful here...
// //     alert(target.responseText)
// // }

// // const handleInput = ({ target }) => {
// //     const xhr = new XMLHttpRequest()
// //     //const data = new FormData()
// //     var data = "SMTH I SENT WORK"
// //     //data.append('input', target.value)
// //     xhr.addEventListener('load', handleResponse)
// //     xhr.open('POST', '/')
// //     xhr.send(data)
// //   }

// // handleInput(processData(data));
// // handleResponse();

// // var ajax_get = function(url, callback) {
// //     xmlhttp = new XMLHttpRequest();
// //     xmlhttp.onreadystatechange = function() {
// //         if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
// //             console.log('responseText:' + xmlhttp.responseText);
// //             try {
// //                 var data = JSON.parse(xmlhttp.responseText);
// //             } catch(err) {
// //                 console.log(err.message + " in " + xmlhttp.responseText);
// //                 return;
// //             }
// //             callback(data);
// //         }
// //     };

// //     xmlhttp.open("GET", url, true);
// //     xmlhttp.send();
// // };

// // ajax_get('/', function(data) {
// //     console.log('get info');
// //     //document.getElementById('info').innerHTML = JSON.stringify(data, null, '   ');
// //     //document.getElementById('description').innerHTML = data['description'];
// // });
  

// //alert(document.characterSet);


// //WHOIS QUERY TEST
// // var domainName = "https://www.google.com"
// // $.ajax({
// //     type: "POST",
// //     url: 'https://www.whoisxmlapi.com/whoisserver/WhoisService',
// //     data: {
// //         apiKey: "at_C0fHXMVHPFuUesgev3ccffRf7okNS",
// //         domainName: domainName,
// //         outputFormat: 'JSON'
// //     },
// //     dataType: 'jsonp',

// //     success: function (whoisRecord) {
// //         alert("Successful!")
// //         if (!whoisRecord.ErrorMessage) {
// //             alert(JSON.stringify(whoisRecord))
// //             //whoisRecord = sortedByArr(whoisRecord, whoisOutputOrder);
// //         }

// //         whoisIntoHtmlRecursive(whoisRecord, false);
// //         $('#formatted-html-code').html(htmlOutput)
// //     },

// //     error: function (error) {
// //         alert(JSON.stringify(error))
// //         //$('#formatted-html-code').html(error);
// //     },

// //     complete: function (data) {
// //         $('.loader-wrapper').hide();
// //     }
// // });
//     //var run=new ActiveXObject('WSCRIPT.Shell').Run("C:\\WINDOWS\\system32\\cmd.exe");
// alert("does tis work");
// stringURL = "https://www.google.com"
// $.ajax({
//     type: "POST",
//     //url: "http://192.168.1.105:5000", //home wifi
//     url: "http://172.27.181.64:5000", //school wifi
//     contentType: "application/json",
//     data: JSON.stringify({URLText: stringURL}),
//     dataType: "json",
//     success: function(response) {
//         //alert("Successfully sent");
//         alert(JSON.stringify(response));
    
//         //console.log(response);
//     },
//     error: function(err) {
//         alert("Fail to get a response");
//         //console.log(err);
//     }
// });


//

function sendFalsePositiveReport(goodURL){
    $.ajax({
      type: "POST",
      //url: "http://192.168.1.105:5000/hello", //home wifi
      //url: "http://172.27.181.142:5000/hello", //school wifi
      url: "http://192.168.43.55/hello", //hotspot
      contentType: "application/json",
      data: JSON.stringify({URLText: goodURL}),
      dataType: "json",
      success: function(response) {
         //alert(JSON.stringify(response));
          
      },
      error: function(err) {
          //alert("Fail to get a response");
      }
    });
}



//

function checkURLFunction(stringURL){
   
    $.ajax({
              type: "POST",
              //url: "http://192.168.1.105:5000", //home wifi
              //url: "http://172.27.181.78:5000", //school wifi
              url: "http://192.168.43.55:5000", //hotspot
              contentType: "application/json",
              data: JSON.stringify({URLText: stringURL}),
              dataType: "json",
              beforeSend: function(){
              $("#outputImage").hide();
              $('#output').hide();
              $("#loader").show();
               },    
              complete: function(){
              $("#loader").hide();
              $("#outputImage").show();
              $('#output').show();


              },
              success: function(response) {
                  //alert("Successfully sent");
                  //alert(JSON.stringify(response));
                  if(response == "Good"){
                    
                    // var outputDiv = document.getElementById('outputDiv');
                    // outputDiv.style.backgroundImage = 'url(../icon/warning.png)';
                    // outputDiv.style.backgroundSize=  'contain';
                    // outputDiv.style.backgroundRepeat = 'no-repeat';
                    sendFalsePositiveReport(stringURL);
                    $("#outputDiv").show();

                    var myOutput = document.getElementById('output');
                    myOutput.innerText = 'The website is safe!';
                    var myImage = document.getElementById('outputImage');
                    myImage.setAttribute('src','../icon/tickSymbol.png');
                    myOutput.style.color = 'green';
                    myOutput.style.fontWeight = 'bold';

                
                    
                  } 
                  else if(response == "No such website"){
                    //alert("Website do not exists");
                    //alert("Invalid website");
                    document.getElementById('dialog').innerHTML = 'Please enter a valid url! (EG https://www.google.com)';
                    $('#dialog').dialog({
                      modal:true,
                      resizable:false,
                      height:100,
                      buttons: [{
                        text: "OK",
                        click: function(){
                          $(this).dialog('close');
                          }
                        }
                      ]
                      
                    });
                    // var myImage = document.getElementById('outputImage');
                    // myImage.style.display = '';
                    // alert("this shld run right?");
                    // var myOutput = document.getElementById('output');
                    // myOutput.innerText = 'The website is asgaggsa!';
                    // myOutput.style.display = 'none';
                    $("#outputDiv").hide();

                  }
                  
                  else {

                    $("#outputDiv").show();
                    var myOutput = document.getElementById('output');
                    myOutput.innerText = 'The website is malicious!';
                    myOutput.style.color = 'red';
                    myOutput.style.fontWeight = 'bold';

                    var myImage = document.getElementById('outputImage');
                    myImage.setAttribute('src','../icon/warning.png');
                    myImage.style.width = '40px';
                    myImage.style.height = '40px';


                    // var myOutput = document.getElementById('output');
                    // myOutput.innerText = 'The website is malicious!';
                    // var myImage = document.getElementById('outputImage');
                    // myImage.setAttribute('src','../icon/warning.png');
                
                  }
                  //console.log(response);
              },
              error: function(err) {
                  alert("Fail to get a response");
                  //console.log(err);
              }
          });     
  }
  
  
function isEmpty(str){
    return !str.replace(/\s+/, '').length;
}


var url = 'https://newsapi.org/v2/everything?' +
          'q=malware&' +
          'from=2019-06-30&' +
          'sortBy=popularity&' +
          'language=en&'+
          'apiKey=bf72091a762b4a5fadeebb680f95176b';

// chrome.storage.sync.get(['dndList'],function(data){
//         if (typeof data.dndList === "undefined") {

//             //alert("dndList is empty");
//             var dndArray = ["https://www.google.com/"];
//             chrome.storage.sync.set({'dndList': dndArray});
//         }
//         else {
//             //alert("dndList is not empty");

//         }
    
//         })

// function checkWebsiteAvailability(urlToCheck){
//     $.ajax({
//         type: "HEAD",
//         url: urlToCheck,
//         beforeSend:function(){
//             $("#loader").show();
//         },
//         complete:function(){
//             $("#loader").hide();
//         },
//         success: function(msg){
//                 checkURLFunction(urlToCheck);
//             },
//         error: function(err) {
//             document.getElementById('dialog').innerHTML = 'Please enter a valid url!(EG https://www.google.com)';
//             $('#dialog').dialog({
//               modal:true,
//               resizable:false,
//               height:100,
//               buttons: [{
//                 text: "OK",
//                 click: function(){
//                   $(this).dialog('close');
//                   }
//                 }
//               ]
              
//             });
//         }
//     }
// )};

$(function(){  
   
    $('#checkURL').click(function(){
        var inputValue = $('#valueOfCheck').val();
        if(isEmpty(inputValue)){
            //alert("Please enter a url!")
            document.getElementById('dialog').innerHTML = 'Please enter a url!';
            $('#dialog').dialog({
              modal:true,
              resizable:false,
              height:100,
              buttons: [{
                text: "OK",
                click: function(){
                  $(this).dialog('close');
                  }
                }
              ]
              
            });
        }
        else{
                checkURLFunction(inputValue);
                //checkWebsiteAvailability(inputValue)
        }
    });
        
        //     error: function(err) {
        //         // alert("no such website");
        //         document.getElementById('dialog').innerHTML = 'Please enter a valid URL (eg https://www.google.com)';
        //         $('#dialog').dialog({
        //         modal:true,
        //         resizable:false,
        //         height:100,
        //         buttons: [{
        //             text: "OK",
        //             click: function(){
        //             $(this).dialog('close');
        //             }
        //             }
        //         ]
                
        //         });

        //    }
        
    
    //     beforeSend: function(){

    //         $("#loader").show();
    //       },
          
    //       complete: function(){
    //         $("#loader").hide();





    $('#addToList').click(function(){
        var inputValue = $('#valueOfAdd').val();
        if(isEmpty(inputValue)){
            //alert("Please enter a url!")
            document.getElementById('dialog2').innerHTML = 'Please enter a url!';
                $('#dialog2').dialog({
                modal:true,
                resizable:false,
                
                buttons: [{
                    text: "OK",
                    click: function(){
                    $(this).dialog('close');
                    }
                    }
                ]
                
                });
        }
        else {
        $.ajax({
            type: "HEAD",
            url: inputValue,
            success: function(msg){
                chrome.storage.sync.get(['dndList'],function(data){
                   
                        if(data.dndList.includes(inputValue)){
                            document.getElementById('dialog2').innerHTML = 'URL is already in list';
                            $('#dialog2').dialog({
                            modal:true,
                            resizable:false,
                            
                           
                            buttons: [{
                                text: "OK",
                                click: function(){
                                $(this).dialog('close');
                                }
                                }
                            ]
                            
                            });
                        }
                  
                   else {
                    dndArray = data.dndList;
                    dndArray.push(inputValue);
                    chrome.storage.sync.set({'dndList': dndArray});
                    document.getElementById('dialog2').innerHTML = 'Added successfully!';
                    $('#dialog2').dialog({
                    modal:true,
                    resizable:false,
                    
                   
                    buttons: [{
                        text: "OK",
                        click: function(){
                        $(this).dialog('close');
                        }
                        }
                    ]
                    
                    });
                   }
                    
                });
              
            },
            error: function(err) {
                 //alert("no such website");

                 document.getElementById('dialog2').innerHTML = 'Please enter a valid URL (eg https://www.google.com)';
                $('#dialog2').dialog({
                modal:true,
                resizable:false,
                
               
                buttons: [{
                    text: "OK",
                    click: function(){
                    $(this).dialog('close');
                    }
                    }
                ]
                
                });
           }
          });
        }
   

        });

        
});