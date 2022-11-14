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

// Character remaining counter
$(document).ready(function () {
	var start = 0;
	var limit = 2000;

	$("#message").keyup(function () {
		start = this.value.length;
		if (start > limit) {
			return;
		} else if (start === 2000) {
			$("#remaining").html(`${limit - start} characters remaining`).css("color", "red");
			swal("Opsss!", "Character limit reached", "info");
		} else if (start > 1500) {
			$("#remaining").html(`${limit - start} characters remaining`).css("color", "red");
		} else if (start < 2000) {
			$("#remaining").html(`${limit - start} characters remaining`).css("color", "darkgray");
		} else {
			$("#remaining").html(`${limit} characters remaining`).css("color", "#0f675150");
		}
	});
});
// Limit upload file size to 10MB
$(document).ready(function() {
	const upload = document.getElementById('file');
	upload.onchange = function() {
		if (this.files[0].size > 10 * 1048576) {
			swal('File Too Large', "Maximum upload limit is 10MB", 'info');
			this.value = "";
		};
	};
});


