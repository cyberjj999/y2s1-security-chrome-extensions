// function dragStart(ev) {
//     ev.dataTransfer.effectAllowed='move';
//     ev.dataTransfer.setData("Text", ev.target.getAttribute('id'));
//     ev.dataTransfer.setDragImage(ev.target,0,0);
//     //return true;
//  }
//  function dragEnter(ev) {
//     event.preventDefault();
//     //return true;
//  }
//  function dragOver(ev) {
//     //return false;
//  }
//  function dragDrop(ev) {
//      alert("wtf wtf wtf");
//     var src = ev.dataTransfer.getData("Text");
//     alert(document.getElementById(src));
//     ev.target.removeChild(document.getElementById(src));
//     //ev.stopPropagation();
//     //return false;
//  }

$(document).ready(function() {
    var id;
    function allowDrop(ev)
    {
    ev.preventDefault();
    }

    //this runs everytime i drag a element up (inside the method i will "hold" the element's id)
    function drag(ev)
    {
        //every element i created dynamically has an id , i "hold" onto their id everytime this runs
        id = ev.target.id;
    //alert(id);
    //ev.dataTransfer.setData("Text",this.id);
    //alert(this.id);
    }
    
    //This event run every time i drop a certain element into the trashbin
    //Other areas are not allowed so only when towards trashbin will run
    function drop(ev)
    //i make changes to the jquery.ui css , replace the images/../.. to
    //../images/../.. , cause i moved it to css folder , so it needs to be placed 1 folder above
    
    {
        //change the inside text of dialog
        document.getElementById('dialog').innerHTML = 'Are you sure you want to remove this URL?';
        $('#dialog').dialog({
          modal:true,
          resizable:false,
          height:120,
          class: 'dialogStyle',
          buttons: [
            {
              text: "Yes",
              class:'green',
                click:function(){
                    //retrieving that particular element , then remove it
                    var el = document.getElementById(id);
                    el.parentNode.removeChild(el);

                    //get current list of dndList
                    chrome.storage.sync.get(['dndList'],function(data){
                        var myArr = data.dndList;
                        for(var i=0;i<myArr.length;i++){
                            //loop through the list , if the id(which i held just now)
                            //is same as the value of the element
                            //remove that element P.S id is eg https://www.google.com1
                            //use substring cus i need remove the "1" , so i can identify
                            if ( myArr[i] === id.substring(0,(id.length-1))) {
                                myArr.splice(i, 1); 
                                //alert("my array is " + myArr);
                                chrome.storage.sync.set({'dndList': myArr});
                              }
                        }
                        
                        });
                    $(this).dialog('close');

                }
            },
            {
              text: "No",
              class:'red',
              click:function(){
                $(this).dialog('close');
              }
            }
          ]
        });
            
    
    // ev.preventDefault();
    // var data=ev.dataTransfer.getData("Text");
    // alert(data);
    // var el = document.getElementById(data).value;
    // alert(el);
    // el.parentNode.removeChild(data);
    
    }
     //    var newCell = document.createElement('td');
        //     newCell.innerText = data.dndList[i]
    chrome.storage.sync.get(['dndList'],function(data){
        
        // var perrow = 1; // 3 items per row
        var newTable = document.createElement('table');
        //var newRow = document.createElement('tr');
        //newTable.appendChild(newRow);
        //html = "<table><tr>";

        for (var i=0; i<data.dndList.length; i++) {
        var newCell = document.createElement('td');
        newCell.innerText = data.dndList[i];
        newCell.setAttribute('draggable',"true");
        newCell.setAttribute('id',data.dndList[i]+i);    
        newCell.ondragstart = function(){    
            drag(event)
            //dragStart(event);
            // var content = newCell.innerText;
            // alert(content);
        };
        //newCell.setAttribute('ondragstart','drag(event)');
        //     newCell.setAttribute('style','background-color:red;')
         
        //var newCell = "<td>" + data.dndList[i] + "</td>";
        var newRow = document.createElement('tr');
        newRow.appendChild(newCell);
        newTable.appendChild(newRow);

        //html += newCell;
        // Break into next row
        // var next = i+1;
        // if (next%perrow==0 && next!=data.dndList.length) {
        //   //html += "</tr><tr>";
        //   var anotherRow = document.createElement('tr');
        //   newTable.appendChild(anotherRow);

        //     }
        }


        //html += "</tr></table>";    
        //document.getElementById("container").innerHTML = html;
        document.getElementById("container").appendChild(newTable);
        trashbin = document.getElementById('deleteArea');
        //trashbin.setAttribute('ondrop','dragDrop(event)')
        trashbin.ondrop = function(){
            drop(event);
          
            //dragDrop(event);
        }
        trashbin.ondragover = function(){
            allowDrop(event)       
            //dragOver(event); 
        }

        // trashbin.ondragenter = function(){
        //     dragEnter(event);
        // }
        // trashbin.setAttribute('ondrop','drop(event)')
        // trashbin.setAttribute('ondragover','allowDrop(event)');
    });


});