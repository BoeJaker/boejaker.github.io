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

// $(document).ready(function() {

//   $('a').hoverIntent(function() {
//       $(this).removeClass('active');
//       setTimeout(function(){
//         $(this).addClass('temp');
//       },500);
//     },
//     function() {
//       $(this).addClass('active');
      
//     $(this).removeClass('temp');
//     }
//   );

// });


$(window).scroll(function(){
	if ($("page").outerHeight() <= $(window).height() ) {
	clearTimeout($.data(this, 'scrollTimer'));
	$.data(this, 'scrollTimer', setTimeout(function() {
		var individualDivHeight = $('page').height();
		var _cur_top = $(window).scrollTop();
		var totalHeight = $('content').height();
		var posToScroll = Math.round(_cur_top / individualDivHeight) * individualDivHeight;

		$('html, body').stop().animate({scrollTop: posToScroll}, 200);
	}, 250));
		};
});
$('page').on('touchmove', function() {
  if ($('page').outerHeight() <= $(window).height()) {
    clearTimeout($.data(this, 'scrollTimer'));
    $.data(this, 'scrollTimer', setTimeout(function() {
      var individualDivHeight = $('page').height();
      var _cur_top = $(window).scrollTop();
      var totalHeight = $('content').height();
      var posToScroll = Math.round(_cur_top / individualDivHeight) * individualDivHeight;
      // Use native browser scrolling instead of jQuery's animate()
      $('html, body').css('scroll-behavior', 'smooth');
      window.scrollTo({ top: posToScroll, behavior: 'smooth' });
      $('html, body').stop().animate({scrollTop: posToScroll}, 200);
    }, 250));
  }
});

