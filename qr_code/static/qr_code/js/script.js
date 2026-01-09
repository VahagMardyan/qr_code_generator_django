document.addEventListener('keyup',(event) => {
    event.shiftKey && event.key === "Enter" ? document.getElementById("url").focus() : null;
});

const btn_download = document.getElementById('btn-download');

if(btn_download) {
    btn_download.addEventListener('click', ()=>{
        const img = document.querySelector('#img-block img');
        if(!img) return;
        const link = document.createElement('a');
        link.href = img.src;
        link.download = "qr_code.png";
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    });    
}

