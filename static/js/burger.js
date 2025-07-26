function toggleNavbar() {
  var x = document.getElementById("myNavbar");
  if (x.className === "navbar-bur") {
    x.className += " responsive";
  } else {
    x.className = "navbar-bur";
  }
}
