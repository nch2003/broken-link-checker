//navbar stays sticky while scrolling
window.addEventListener("scroll" , function() {
    var nav = this.document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 0);
});

//hamburger-menu appears when the resolution is changing
var menu = document.querySelector(".menu");
var menuBTN = document.querySelector(".menu-btn");
var closeBTN = document.querySelector(".close-btn", "");

menuBTN.addEventListener("click", () => {
    menu.classList.add("active");
});

closeBTN.addEventListener("click", () => {
    menu.classList.remove("active");
});

document.addEventListener("click", (e) => {
    // Check if the click target is not part of the menu or menu button
    if (e.target !== menu && e.target !== menuBTN) {
        menu.classList.remove("active");
    }
});

document.getElementById('home-link').addEventListener('click', function () {
    // Face scroll la elementul principal
    document.querySelector('.container').scrollIntoView({
        behavior: 'smooth'
    });
});

