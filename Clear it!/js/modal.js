// $(".Clear").click(function (){
//     alert('Clearing browsing history now...');

// });

// $("#Cancel").click(function (){
//     alert('Clearing browsing history now...');

// });


$(function(){
    var x = 0;
    var p = 0;
    document.getElementById("1hour").style["box-shadow"] = "0px 0px 3px #000000"; 


  $('#1hour').click(function(){

    document.getElementById("1hour").style["box-shadow"] = "0px 0px 3px #000000";
    document.getElementById("1day").style["box-shadow"] = "None";
    document.getElementById("1week").style["box-shadow"] = "None";
    x = 0;
    // $("#userInput").val() == "";
    // $("#userInput").innerHTML == "";
    document.getElementById('userInput').value = '';

  })
  $('#1day').click(function(){

    document.getElementById("1day").style["box-shadow"] = "0px 0px 3px #000000";
    document.getElementById("1hour").style["box-shadow"] = "None";
    document.getElementById("1week").style["box-shadow"] = "None";
    x = 1;

    document.getElementById('userInput').value = '';

  })
  $('#1week').click(function(){
 
    document.getElementById("1week").style["box-shadow"] = "0px 0px 3px #000000";
    document.getElementById("1hour").style["box-shadow"] = "None";
    document.getElementById("1day").style["box-shadow"] = "None";
    x = 2;
    document.getElementById('userInput').value = '';

  })

  $('#userInput').click(function(){
    document.getElementById("1week").style["box-shadow"] = "None";
    document.getElementById("1hour").style["box-shadow"] = "None";
    document.getElementById("1day").style["box-shadow"] = "None";
    x = -1;

  });
    
    $('#Cancel').click(function(){
      
      // x = document.getElementById('userInput').value;
      // if (x==-1){
      //   alert("please input smth");
      // }
      chrome.runtime.sendMessage({type:'clearedData'});

    });
    
    $('#Clear').click(function(){
        p = document.getElementById('userInput').value;
        if( ($("#userInput").val() == "" || $("#userInput").val() == null) && x==-1 ){
          document.getElementById('dialog').innerHTML = 'Please select an option!';
          $('#dialog').dialog({
            modal:true,
            resizable:false,
            height:140,
            buttons: [{
              text: "OK",
              click: function(){
                $(this).dialog('close');
                }
              }
            ]
            
          });
          p = 0;
        }

        else {
       
        //true by default
        if(x == 0 && p ==0) {
          //1 hour
          //var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;

        var millisecondsPerWeek = 1000 * 60 * 60;
        var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
        clearData(oneWeekAgo);
        }
        else if(x == 1 && p ==0) {
          //1 day
        var millisecondsPerWeek = 1000 * 60 * 60 * 24;
        var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
        clearData(oneWeekAgo);

        } 
          //1 week
        else if(x == 2 && p ==0) {

        var millisecondsPerWeek = 1000 * 60 * 60 * 24 * 7;
        var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
        clearData(oneWeekAgo);
       
        }

        else if (p==-1){
          //set it to 0 to clear everything
          //var millisecondsPerWeek = 0;
          //var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
          var oneWeekAgo = 0;
          clearData(oneWeekAgo);
        }
        else if (p==0 || p<0 || p>9999){
          document.getElementById('dialog').innerHTML = 'Please enter a valid number (1-9999)';
          $('#dialog').dialog({
            modal:true,
            width:400,
            resizable:false,
            height:140,
            buttons: [{
              text: "OK",
              click: function(){
                $(this).dialog('close');
                }
              }
            ]
            
          });
        }
        else if (p!=0){
          var millisecondsPerWeek = 1000 * 60 * 60 * p;
          var oneWeekAgo = (new Date()).getTime() - millisecondsPerWeek;
          clearData(oneWeekAgo);
        }

      }

    });
    
});



function clearData(oneWeekAgo) {
    document.getElementById('dialog').innerHTML = 'Are you sure?';

    // Do something clever here once data has been removed.
    $('#dialog').dialog({
      modal:true,
      resizable:false,
      class: 'dialogStyle',
      buttons: [
        {
          text: "Yes",
          class:'green',
            click:function(){
              chrome.browsingData.remove({
                "since": oneWeekAgo
              }, {
                "appcache": true,
                "cache": true,
                "cacheStorage": true,
                "cookies": true,
                "downloads": true,
                "fileSystems": true,
                "formData": true,
                "history": true,
                "indexedDB": true,
                "localStorage": true,
                "pluginData": true,
                "passwords": true,
                "serviceWorkers": true,
                "webSQL": true
              });
              
              //$(this).dialog('close');
              document.getElementById('dialog').innerHTML = 'Data has been cleared successfully!';
              $('#dialog').dialog({
                modal:true,
                resizable:false,
                height:140,
                buttons: [{
                  text: "OK",
                  click: function(){chrome.runtime.sendMessage({type:'clearedData'})
                    }
                  }
                ]
                
              });

            }
        },
        {
          text: "No",
          class:'red',
          click:function(){
            //reset to original value
            x = 0;
            p = 0;
            $(this).dialog('close');
          }
        }
      ]
    });
    

};


//   var r = confirm("Are you sure you want to clear browsing data?!");
//   if (r == true) {
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


/*
var r = confirm("Are you sure you want to clear browsing data?!");

  if (r == true) {
  chrome.browsingData.remove({
    "since": oneWeekAgo
  }, {
    "appcache": true,
    "cache": true,
    "cacheStorage": true,
    "cookies": true,
    "downloads": true,
    "fileSystems": true,
    "formData": true,
    "history": true,
    "indexedDB": true,
    "localStorage": true,
    "pluginData": true,
    "passwords": true,
    "serviceWorkers": true,
    "webSQL": true
  });
  
  alert("Data has been cleared");
  chrome.runtime.sendMessage({type:'clearedData'});
  
    
 
}

else {
    //alert("Data has not been cleared");
    // $('#dialog').dialog({
    //   modal:true,
    //   resizable:false,
    //   buttons: [
    //     {
    //       text: "Yes",
    //         click:function(){
    //           alert("You say okay!");
    //         }
    //     },
    //     {
    //       text: "No",
    //       click:function(){
    //         $(this).dialog('close');
    //       }
    //     }
    //   ]
    // });
}
*/