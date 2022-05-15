function a(el) {
	var b=document.getElementById(el);
	if (b.hasAttribute("hidden")) {
		document.getElementById(el).removeAttribute("hidden");
	}
	else {
		document.getElementById(el).setAttribute("hidden", true);
	}
}

