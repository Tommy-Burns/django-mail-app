// Function to pulsate text at login page

$(document).ready(() => {
	(function pulse() {
		$(".text-pulse").fadeOut(1000).fadeIn(1000, pulse);
	})();
});

// Hide or show password
function myFunction() {
	var p = document.getElementById("password");
	if (p.type === "password") {
		p.type = "text";
	} else {
		p.type = "password";
	}
}
