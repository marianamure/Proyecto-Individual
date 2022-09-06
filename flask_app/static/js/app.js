
function change() {
    document.getElementById("chg").src="../static/images/seed16.jpg"
}

function change2() {
    document.getElementById("chg").src="../static/images/planta2.png"
}


//popup

var deleteLinks = document.querySelectorAll('.delete');

for (var i = 0; i < deleteLinks.length; i++) {
    deleteLinks[i].addEventListener('click', function(event) {
        event.preventDefault();

    var choice = confirm(this.getAttribute('data-confirm'));

	if (choice) {
	    window.location.href = this.getAttribute('href');
	}
  });
}