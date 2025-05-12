// JavaScript
window.addEventListener('scroll', function() {
    var navbar = document.querySelector('nav');
    var heroSection = document.querySelector('.hero');
    var cardsSection = document.querySelector('.cards');

    if (window.scrollY > heroSection.offsetHeight && window.scrollY < (heroSection.offsetHeight + cardsSection.offsetHeight)) {
        navbar.classList.add('scrolled'); // Tambah class 'scrolled' saat background image tertutup
    } else {
        navbar.classList.remove('scrolled'); // Hapus class 'scrolled' saat background image masih terlihat
    }
});

function openNav() {
    document.getElementById("mySidebar").style.width = "250px";
    // Mengubah margin-left menjadi 0 agar button tidak bergeser
    document.getElementById("main").style.marginLeft = "0";
  }
  
  function closeNav() {
    document.getElementById("mySidebar").style.width = "0";
    document.getElementById("main").style.marginLeft= "0";
  }

  var toggleButton = document.getElementById('toggle-button');

  toggleButton.addEventListener('click', function() {
    document.body.classList.toggle('dark-mode');
  });  

  $(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        responsive: {
            0: {
                items: 2 // di layar yang lebarnya 0px ke atas, tampilkan 2 item
            },
            768: {
                items: 4 // di layar yang lebarnya 768px ke atas, tampilkan 4 item
            }
        }
    });
});
