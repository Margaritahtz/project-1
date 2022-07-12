let socket = new WebSocket('ws://localhost:8000/ws/polData/');

var websocketList = [];

socket.onopen= function(e){
 alert('connection established');
};

socket.onmessage = function(e){
   console.log(e.data);
   document.getElementById("demo").innerHTML = "Temperature:" + e.data;
   var recData=JSON.parse(e.data);
   dataObjNew=dataObj['data']['datasets'][0]['data'];
   dataObjNew.shift();
   dataObjNew.push(recData.value);
   dataObj['data']['datasets'][0]['data']=dataObjNew;
   window.myLine.update();

};


socket.onclose = function(e){
 alert('connection closed');
};






