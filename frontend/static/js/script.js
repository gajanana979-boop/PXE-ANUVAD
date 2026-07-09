const form = document.getElementById("translateForm");

const fileInput = document.getElementById("file");

const dropZone = document.getElementById("dropZone");

const selectedFile = document.getElementById("selectedFile");

const progress = document.getElementById("progress");

const resultCard = document.getElementById("resultCard");

const downloadBtn = document.getElementById("downloadBtn");

const translateBtn = document.getElementById("translateBtn");



// -------------------------
// File Selection
// -------------------------

fileInput.addEventListener("change", () => {

    if(fileInput.files.length){

        selectedFile.innerHTML =
        "📄 " + fileInput.files[0].name;

    }

});



// -------------------------
// Drag & Drop
// -------------------------

dropZone.addEventListener("dragover",(e)=>{

    e.preventDefault();

    dropZone.classList.add("dragover");

});

dropZone.addEventListener("dragleave",()=>{

    dropZone.classList.remove("dragover");

});

dropZone.addEventListener("drop",(e)=>{

    e.preventDefault();

    dropZone.classList.remove("dragover");

    fileInput.files=e.dataTransfer.files;

    if(fileInput.files.length){

        selectedFile.innerHTML=
        "📄 "+fileInput.files[0].name;

    }

});

dropZone.addEventListener("click",()=>{

    fileInput.click();

});



// -------------------------
// Translate
// -------------------------

form.addEventListener("submit",async(e)=>{

    e.preventDefault();

    if(fileInput.files.length===0){

        alert("Please select a document.");

        return;

    }

    progress.style.display="block";

    resultCard.style.display="none";

    translateBtn.disabled=true;

    translateBtn.innerHTML=
    '<i class="fa-solid fa-spinner fa-spin"></i> Translating...';

    const formData=new FormData(form);

    try{

        const response=await fetch("/translate",{

            method:"POST",

            body:formData

        });

        const result=await response.json();

        progress.style.display="none";

        translateBtn.disabled=false;

        translateBtn.innerHTML=
        '<i class="fa-solid fa-language"></i> Translate Document';

        if(result.success){

            resultCard.style.display="block";

            downloadBtn.href=result.download_url;

        }

        else{

            alert(result.message);

        }

    }

    catch(error){

        progress.style.display="none";

        translateBtn.disabled=false;

        translateBtn.innerHTML=
        '<i class="fa-solid fa-language"></i> Translate Document';

        alert("Translation failed.");

    }

});