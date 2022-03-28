function a() {
	var b=document.getElementById("espace_fumeur");
	if (b.hasAttribute("hidden")) {
		document.getElementById("espace_fumeur").removeAttribute("hidden");
	}
	else {
		document.getElementById("espace_fumeur").setAttribute("hidden", true);
		b.style="width=1px","height:1px";
	}
	
	
}

function b() {
	var a=document.getElementById("Jour").value;
	if (a=="Lundi") {
		location.reload();
	}
	if (a=="Mardi") {
		document.getElementById("valeurmin").innerHTML="4";
		document.getElementById("valeurmoy").innerHTML="12";
		document.getElementById("valeurmax").innerHTML="15";
	}
}