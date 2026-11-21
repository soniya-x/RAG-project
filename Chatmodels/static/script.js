async function sendMessage(){

    const msg=document.getElementById("message").value;
    const mode=document.getElementById("mode").value;

    if(msg==="") return;

    const chat=document.getElementById("chatBox");

    chat.innerHTML +=
    `<div class="user">
        <span>${msg}</span>
    </div>`;

    document.getElementById("message").value="";

    const response=await fetch("/chat",{

        method:"POST",

        headers:{
            "Content-Type":"application/json"
        },

        body:JSON.stringify({

            message:msg,
            mode:mode

        })

    });

    const data=await response.json();

    chat.innerHTML +=
    `<div class="bot">
        <span>${data.reply}</span>
    </div>`;

    chat.scrollTop=chat.scrollHeight;

}