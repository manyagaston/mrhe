const activePage = window.location.pathname;
const navLinks = document.querySelectorAll(".navbar a");
const searchIcon = document.querySelector(".search-box a");
const header = document.querySelector("header");
const newsLetterBtn = document.getElementById("news-letter-btn");
const contactBtn = document.getElementById("contact-btn");

// Get the button
let mybutton = document.getElementById("btn-back-to-top");


// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  // adding box-shadaw on header while user is scrolling
  header.classList.add("navbar-shadaw")
  scrollFunction();
};

function scrollFunction() {
  if (
    document.body.scrollTop > 20 ||
    document.documentElement.scrollTop > 20
  ) {
    mybutton.style.display = "block";
    
  } else {
    mybutton.style.display = "none";
  }
}
// When the user clicks on the button, scroll to the top of the document
mybutton.addEventListener("click", backToTop);

function backToTop() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

navLinks.forEach(link =>{
 if (link.href.includes(`${activePage}`)) {
    link.classList.add("activeLink");
    if (activePage == '/'){
      link.classList.remove("activeLink")
    }
  }
})

// Stop page refresh when user click on newsletter button

newsLetterBtn.addEventListener('click', (e)=>{
  e.preventDefault();
})

// Stop page refresh when user click on contact button

/*contactBtn.addEventListener('click', (e)=>{
  e.preventDefault();
})*/




