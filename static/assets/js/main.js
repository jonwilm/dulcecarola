$(window).on("load", function() {
  $(".preloader").fadeOut(500)
  
  changeHeightNavbar();
  
  $(window).scroll(function () {
    changeHeightNavbar();
  });
  $(window).resize(function () {
    changeHeightNavbar();
    console.log('resize')
  });
  
  function changeHeightNavbar() {
    if ($(window).width() > 992) {
      if ($(window).scrollTop() > 80) {
        $(".navbar").css("height", "55px");
        $(".logo-navbar").css("height", "40px");
      } else {
        $(".navbar").css("height", "75px");
        $(".logo-navbar").css("height", "50px");
      }
    } else if ($(window).width() < 360) {
      $(".navbar").css("height", "65px");
      $(".logo-navbar").css("height", "23px");
    } else {
      $(".navbar").css("height", "65px");
      $(".logo-navbar").css("height", "40px");
    }
  }
  var menuMobileOpen = false
  function openCloseNavMobile() {
    if (!menuMobileOpen) {
      $('.nav-mobile').css('right', '0')
      menuMobileOpen = true
    } else {
      $('.nav-mobile').css('right', '-100%')
      menuMobileOpen = false
    }
  }
  $('#open-menu').click(function() {
    openCloseNavMobile()
  })
})
// ------------------------------------------------------------
// AUTOMATIC DROPDOWN
// ------------------------------------------------------------
$(".dropdown").hover(function() {
  if ($(window).width() > 1200) {
    $("a", this).addClass("show");
    $("a", this).attr("aria-expanded", "true");
    $(".dropdown-menu", this).addClass("show");
    $(".dropdown-menu", this).attr("data-bs-popper", "none");
  }
}, function() {
  if ($(window).width() > 1200) {
    $("a", this).removeClass("show");
    $("a", this).attr("aria-expanded", "false");
    $(".dropdown-menu", this).removeClass("show");
    $(".dropdown-menu", this).removeAttr("data-bs-popper");
  }
});
// ------------------------------------------------------------
// BUSCADOR
// ------------------------------------------------------------
$('#link-nav-search').click(function() {
  $('#nav-search').css('display', 'flex')
})
$(document).on("click",function(e) {
  var navSearch = $("#nav-search");
  var linkNavSearch = $("#link-nav-search");
  if (!navSearch.is(e.target) && navSearch.has(e.target).length === 0 && !linkNavSearch.is(e.target) && linkNavSearch.has(e.target).length === 0) { 
    $('#nav-search').css('display', 'none')
  }
});
$('#button-nav-search').click(function() {
  if ($('#input-nav-search').val() != '') {
    let search = $('#input-nav-search').val()
    let url = 'https://www.dulcecarola.com/catalogsearch/result/?q=' + search
    window.open(url)
  } else {
    alert('Ingresa lo que desea buscar')
  }
})
// ------------------------------------------------------------
// MODALS VIDEOS
// ------------------------------------------------------------
let idVideo;
let srcVideo;
$(".btn-video-yt").click(function () {
  idVideo = $(this).attr("id-video");
  srcVideo = "https://www.youtube.com/embed/" + idVideo + "?rel=0;autoplay=1";
});
$("#video-player").on("hidden.bs.modal", function () {
  $("#video-player iframe").attr("src", "");
});
$("#video-player").on("show.bs.modal", function () {
  setTimeout(() => {
    $("#video-player iframe").attr("src", srcVideo);
  }, 100);
});