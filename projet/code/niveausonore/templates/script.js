function a(el) {
	var b=document.getElementById(el);
	if (b.hasAttribute("hidden")) {
		document.getElementById(el).removeAttribute("hidden");
	}
	else {
		document.getElementById(el).setAttribute("hidden", true);
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
