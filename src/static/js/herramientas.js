function loadDoc() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("pizarra").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "/misDocumentos", true);
    xhttp.send();
}

function loadSubirDoc(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("pizarra").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "/formSubir", true);
    xhttp.send();
}

function loadEnviar(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("pizarra").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "Enviar", true);
    xhttp.send();
}






function loadListarUser(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("pizarra").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "accounts/listarUsers", true);
    xhttp.send();
}


function loadDocumentos(){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        document.getElementById("pizarra").innerHTML = this.responseText;
      }
    };
    xhttp.open("GET", "Documentos", true);
    xhttp.send();
}
