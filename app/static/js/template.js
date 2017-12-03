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
// Показати блок реєстраціїї
function registrationBlock() {
    document.getElementById("block2").style.display = "block";
    document.getElementById("first_registration").style.display = "none";
}

// Перевірка двох паролей
window.onload = function () {
    document.getElementById("pass1_reg").onchange = validatePassword;
    document.getElementById("pass2_reg").onchange = validatePassword;
}
function validatePassword(){
var pass2=document.getElementById("pass2_reg").value;
var pass1=document.getElementById("pass1_reg").value;
if(pass1!=pass2)
    document.getElementById("pass2_reg").setCustomValidity("Паролі не співпадають");
else
    document.getElementById("pass2_reg").setCustomValidity(''); // пустая строка означает отсутствие ошибок
}