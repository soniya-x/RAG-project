async function send(){

const msg=document.getElementById("msg").value;

document.getElementById("chat").innerHTML+=
"<div class='user'><b>You:</b> "+msg+"</div>";

const res=await fetch("/chat",{

method:"POST",

headers:{

"Content-Type":"application/json"

},

body:JSON.stringify({

message:msg

})

});

const data=await res.json();

document.getElementById("chat").innerHTML+=
"<div class='bot'><b>Assistant:</b><br>"+data.response+"</div>";

document.getElementById("msg").value="";

}