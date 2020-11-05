function show(){
  document.getElementById("show_div").style.visibility= 'visible' ;
}
document.getElementById("show_button").onclick = function()
{
   show();
   console.log("hello");
};
function show1(){
  document.getElementById("show_div1").style.visibility= 'visible' ;
}
document.getElementById("show_button1").onclick = function()
{
   show1();
   console.log("hello");
};
function show2(){
  document.getElementById("show_div2").style.visibility= 'visible' ;
}
document.getElementById("show_button2").onclick = function()
{
   show2();
   console.log("hello");
};
function show3(){
  document.getElementById("show_div3").style.visibility= 'visible' ;
}
document.getElementById("show_button3").onclick = function()
{
   show3();
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
function hide1(){
  document.getElementById("show_div").style.visibility= 'hidden' ;
}
document.getElementById("hide_button1").onclick = function()
{
   hide1();
   alert("Thank you for making our website better!");
};
function hide2(){
  document.getElementById("show_div").style.visibility= 'hidden' ;
}
document.getElementById("hide_button2").onclick = function()
{
   hide2();
   alert("Thank you for making our website better!");
};
function hide3(){
  document.getElementById("show_div").style.visibility= 'hidden' ;
}
document.getElementById("hide_button3").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button4").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button5").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button6").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button7").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button8").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button9").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
};
document.getElementById("hide_button10").onclick = function()
{
   hide3();
   alert("Thank you for making our website better!");
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
