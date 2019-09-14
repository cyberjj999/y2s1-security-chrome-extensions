function sendFalsePositiveReport(goodURL){
    $.ajax({
      type: "POST",
      //url: "http://192.168.1.105:5000/hello", //home wifi
      //url: "http://172.27.181.142:5000/hello", //school wifi
      url: "http://192.168.43.55:5000/hello", //hotspot

      contentType: "application/json",
      data: JSON.stringify({URLText: goodURL}),
      dataType: "json",
      success: function(response) {
         //alert(JSON.stringify(response));
          
      },
      error: function(err) {
          alert("Fail to get a response");
      }
    });
}

function showMyOptions() {
    var myOptions = document.getElementById("showOptions");
    var proceed = document.getElementById("proceed");
    var mySwitch = document.getElementById('myMLCheckbox');
    var mySlider = document.getElementById('mySwitch');
    var whiteListText = document.getElementById("whitelistText");

  
    if (myOptions.innerText == "Show options") {
      myOptions.innerText = "Unshow options";
    //   btnText.innerHTML = "Read more"; 
      proceed.style.display = "inline-block";
      mySwitch.style.display = "inline-block";
      whiteListText.style.display = "inline-block";
      mySlider.style.display = "inline-block";


    } else {
      myOptions.innerText = "Show options";
    //   btnText.innerHTML = "Read less"; 
      proceed.style.display = "none";
      mySwitch.style.display = "none";
      whiteListText.style.display = "none";
      mySlider.style.display = "none";


    }
  }

$(document).ready(function() {
    chrome.storage.sync.get(['currentMaliciousList'],function(data){
      
        document.getElementById('website').innerText = data.currentMaliciousList;
        

    $('#proceed').click(function(){


      if ($('#myMLCheckbox').prop('checked')){
        chrome.storage.sync.get(['dndList'],function(data2){
          dndArray = data2.dndList;
          dndArray.push(data.currentMaliciousList);
          chrome.storage.sync.set({'dndList': dndArray});

          
        });
        chrome.tabs.update(null,{url:data.currentMaliciousList},function(){

        });
        
        
      }

      else {
        chrome.tabs.update(null,{url:data.currentMaliciousList},function(){
        });
      }
      
    sendFalsePositiveReport(data.currentMaliciousList);

        })

    $('#showOptions').click(function(){
        showMyOptions();
      });

    
});


});

