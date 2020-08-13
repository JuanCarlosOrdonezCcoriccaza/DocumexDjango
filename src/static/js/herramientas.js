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
