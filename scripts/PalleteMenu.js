var windowHeight = $(window).height();
var windowWidth = $(window).width();

function viewport(){
  var st = $(window).scrollTop();
  var wh = $(window).height();
  var top = st;
  var bottom = st + wh;
  
  var dif = $("nav").height() / $(document).height();
  $(".reference").css({
    'height': (wh * dif),
    'top': (st * dif)
  });
}
viewport();
$(window).resize(function(){
  viewport();
});
$(window).scroll(function(){
  viewport();
});
$(document).on('click', 'a[href^="#"]', function (event) {
    event.preventDefault();
    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
}); 

$(document).ready(function() {

  $('a').hoverIntent(function() {
      $(this).removeClass('active');
      setTimeout(function(){
        $(this).addClass('temp');
      },500);
    },
    function() {
      $(this).addClass('active');
    $(this).removeClass('temp');
    }
  );

});