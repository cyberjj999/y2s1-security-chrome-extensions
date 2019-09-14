// alert("this is my favourite website");
//alert("we are at " + location.href);

//chrome.runtime.sendMessage({navigation:'true',url:location.href});
      // "all_frames": true
//^ use that to capture subframe (IF U REALLY WANNA DO)

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
                url: "http://192.168.1.105:5000", //home wifi
                //url: "http://172.27.181.142:5000", //school wifi
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
                        // myFunction(stringURL);
    
                    } 
                    else if(response == "No such website"){
                      alert("Website do not exists");
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
                    alert("Fail to get a response");
                    //console.log(err);
                }
            });
          }
    
          });
     
    }

    function myFunction(maliciousURL) {
  
        chrome.tabs.update(null,{url:"blockpage.html"},function(){
          chrome.storage.sync.set({'currentMaliciousList': maliciousURL});
  
      });
  
  }
//chrome.runtime.sendMessage({navigation:'true',url:location.href});

//alert(location.protocol);
// if (location.protocol == "http:"){
//       //alert("yes its http");
//       checkURL(location.href);
// }

// else {
//   chrome.runtime.sendMessage({navigation:'true',url:location.href});

// }

