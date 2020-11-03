function show(){
  document.getElementById("show_div").style.visibility= 'visible' ;
}
document.getElementById("show_button").onclick = function()
{
   show();
   console.log("hello");
};
function hide(){
  document.getElementById("show_div").style.visibility= 'hidden' ;
}
document.getElementById("hide_button").onclick = function()
{
   hide();
   alert("Thank you for Buying from us!");
};
// When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById("navbar");

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}
