var x = Math.floor((Math.random() * 3) + 1);
if (x==1){
var queryUrl = 'https://newsapi.org/v2/everything?' +
          'q=malware&' +
          'sortBy=popularity&' +
          'language=en&'+
          'apiKey=c7ea39c7010b42249d463a445bcf8c80';
}

else if(x==2){
  var queryUrl = 'https://newsapi.org/v2/everything?' +
  'q=cyber attack&' +
  'sortBy=popularity&' +
  'language=en&'+
  'apiKey=c7ea39c7010b42249d463a445bcf8c80';
}

else if(x==3){
  var queryUrl = 'https://newsapi.org/v2/everything?' +
  'q=hacked&' +
  'sortBy=popularity&' +
  'language=en&'+
  'apiKey=c7ea39c7010b42249d463a445bcf8c80';
}

function queryNewsAPI(){

$.ajax({
    type: "GET",
    url:  queryUrl,
    dataType: "json",
    contentType: "application/json",
    //"http://www.archive.org/download/MIT6.006F11/MIT6_006F11_lec01_300k.mp4"
    //APPARENTLY ITS A HTTP THING , ONLY http can request , for some WEIRD reason
    //data: JSON.stringify({URLText: stringURL}),
    //to send multiple data , do like {URLText: "https://www.google.com",Charset:document.characterSet}

    beforeSend: function(){
        $("#loader").show();
        $("#cyberNews").show();

      },
      
      complete: function(){
        $("#loader").hide();
      },
    success: function(data) {
        document.querySelector("body").style = "display:block";

        var output = "";
        result = JSON.stringify(data)
        //alert(JSON.stringify(data));
        var latestNews = data.articles;
        for(var i in latestNews){   
                output+=`
                <div class="col l6 m6 s12">
                <h4>${latestNews[i].title}</h4>
                <img src="${latestNews[i].urlToImage}" class="responsive-img" style="max-width:100%;
                height:auto;">
                <p>${latestNews[i].description}</p>
                <p>${latestNews[i].content}</p>
                <p>Published on: ${latestNews[i].publishedAt}</p>
                <a href="${latestNews[i].url}">Read more</a>
                </div>
                `;
        }

        if (output!==""){
            $("#newsResults").html(output);

        }
        else{
            var newsNotFound = "Sorry! The news is not available now."
            $("#cybernews").html(newsNotFound);
        }
        //alert("The article is " + JSON.stringify(data.articles));
        //document.write(result);
        // document.getElementById('para1').innerHTML = "Hello";
        // document.getElementById('para2').innerHTML = "Its";
        // document.getElementById('para3').innerHTML = "Me";  

        //Cannnot get elementById for para1 , need to figure out how to do 
        //mayb past tutorial would help?
    },
    error: function(err) {
        var newsNotFound = "Sorry! The news is not available now."
        $("#cybernews").html(newsNotFound);
        //console.log(err);
    }
});
}


queryNewsAPI();

$(document).ready(function(){
    
    $("#searchbtn").on("click",function(e){
      e.preventDefault();
      
      let query = $("#searchquery").val();
    //   let url = 'https://newsapi.org/v2/everything?' +
    //   'q='+query+'&'
    // //   'from=2019-06-30&' +
    //   'sortBy=popularity&' +
    //   'language=en&'+
    //   'apiKey=bf72091a762b4a5fadeebb680f95176b';
    var urlToQuery = 'https://newsapi.org/v2/everything?' +
    'q='+query+'&' +
    'sortBy=popularity&' +
    'language=en&'+
    'apiKey=c7ea39c7010b42249d463a445bcf8c80';
      
      if(query !== ""){
        
        $.ajax({
          
          url: urlToQuery,
          method: "GET",
          dataType: "json",
          
          beforeSend: function(){
            $("#cyberNews").show();
            $("#loader").show();
          },
          
          complete: function(){
            $("#loader").hide();
          },
          
          success: function(news){
            document.getElementById("cybernews").innerHTML = "You searched for " + query;
            let output = "";
            let latestNews = news.articles;
            
            for(var i in latestNews){
              //<div class="col l6 m6 s12">

              output +=`
                <div class="col l6 m6 s12">
                <h4>${latestNews[i].title}</h4>
                <img src="${latestNews[i].urlToImage}" class="responsive-img">
                <p>${latestNews[i].description}</p>
                <p>${latestNews[i].content}</p>
                <p>Published on: ${latestNews[i].publishedAt}</p>
                <a href="${latestNews[i].url}" class="btn">Read more</a>
                </div>
              `;
            }
            
            if(output !== ""){
              $("#newsResults").html(output);
               M.toast({
                html: "There you go, nice reading",
                classes: 'green'
              });
              
            }else{
              let noNews = `<div style='text-align:center; font-size:36px; margin-top:40px;'>This news isn't available. Sorry about that.<br>Try searching for something else </div>`;
               $("#newsResults").html(noNews);
              M.toast({
                html: "This news isn't available",
                classes: 'red'
              });
            }
            
          },
          
          error: function(){
             let internetFailure = `
             <div style="font-size:34px; text-align:center; margin-top:40px;">Please check your internet connection and try again.
             <img src="img/internet.png" class="responsive-img">
             </div>`;
             
            $("#newsResults").html(internetFailure);
             M.toast({
                html: "We encountered an error, please try again",
                classes: 'red'
              });
          }
          
          
        });
        
      }else{
        let missingVal = `<div style="font-size:34px; text-align:center; margin-top:40px;">Please enter any search term in the search engine</div>`;
        $("#newsResults").html(missingVal);
         M.toast({
                html: "Please enter something",
                classes: 'red'
              });
      }
      
    });
    
});