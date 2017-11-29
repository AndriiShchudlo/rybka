jQuery(document).ready(function($) {

	$(".headroom").headroom({
		"tolerance": 20,
		"offset": 50,
		"classes": {
			"initial": "animated",
			"pinned": "slideDown",
			"unpinned": "slideUp"
		}
	});

});
function registrationBlock() {
    document.getElementById("block2").style.display = "block";
    document.getElementById("first_registration").style.display = "none";
}