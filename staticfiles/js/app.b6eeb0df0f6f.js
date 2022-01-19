function openNav() {
  document.querySelector(".nav").classList.add('opennav');
}

// style.width = "25rem";

function closeNav() {
  document.querySelector(".nav").classList.remove('opennav');
}

function openHomeNav() {
  document.querySelector(".nav-links2").style.width = "25rem";
}

function closeHomeNav() {
  document.querySelector(".nav-links2").style.width = "0";
}



function myFunction() {
  /* Get the text field */
  var copyText = document.getElementById("myInput");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied the text: " + copyText.value);
}

var swiper = new Swiper(".mySwiper", {
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  loop: true,
  slidesPerView: 1,
  spaceBetween: 20,

  breakpoints: {
    640: {
      slidesPerView: 2,
      spaceBetween: 30,
    },
    768: {
      slidesPerView: 3,
      spaceBetween: 30,
    },
  },
});

// let header = document.querySelector(".nav");
// console.log(header);


document.onscroll = function() {scrollFunction()};

function scrollFunction() {
  if (document.body.scrollTop > 5 || document.documentElement.scrollTop > 5) {
    document.getElementById("navbar").style.backgroundColor = "#121d33";
  } else {
    document.getElementById("navbar").style.backgroundColor = "transparent";
  }
}
