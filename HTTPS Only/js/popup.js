$(document).ready(function() {

  chrome.storage.sync.get(['httpChecked'],function(data){
      //alert('My current status is ' + data.httpChecked);

    if (data.httpChecked == 'Yes'){
      //alert("checkedYes ran");
      //myCheckbox = document.getElementById('httpCheckbox');
      $("#httpCheckbox").prop("checked", true);
    }
    else {
      //alert("checkedNo ran");
      //myCheckbox = document.getElementById('httpCheckbox');
      $("#httpCheckbox").prop("checked", false);
      //why does it check when i put checked=false
        }
  });


  $('#httpCheckbox').click(function(){

    //when u click, u already checked / unchecked
    if ($('#httpCheckbox').prop('checked')){
      //alert("You are enabling check");
      var checkStatus = 'Yes';
      chrome.storage.sync.set({'httpChecked': checkStatus});
      var opt = {
        type: 'basic',
        title: 'HTTP website blocked',
        message: 'Forcing HTTPS on every website...',
        iconUrl:"icon/noHTTP.png"
        };
        
        chrome.notifications.create(opt);
    }

    else {
      //alert("You are disabling check");
      var checkStatus = 'No';
      chrome.storage.sync.set({'httpChecked': checkStatus});
      var opt = {
        type: 'basic',
        title: 'HTTP website unblocked',
        message: 'Unblocking HTTP on every website...',
        iconUrl:"icon/http.png"
        };
        
        chrome.notifications.create(opt);

        }
 

    });

});











// try{
//     alert(0/0);
// }
// catch{
//     alert("u cannot divide 0 by 0");
// }
// urlToReload = "http://172.26.185.3"
// req.open('GET', urlToReload, false);
              
// req.send(null);

// alert("request sending");
// $.ajax({
//   type: "POST",
//   url: "http://172.26.185.3", //home wifi
//   //url: "http://172.27.181.78:5000", //school wifi
//   contentType: "application/json",
//   //data: JSON.stringify({URLText: stringURL}),
//   dataType: "json",
//   success: function(response) {
//       alert("Successfully sent");
//       //alert(JSON.stringify(response));

//   },
//   error: function(err) {
//       alert("Fail to get a response");
//       //console.log(err);
//   }
// });    