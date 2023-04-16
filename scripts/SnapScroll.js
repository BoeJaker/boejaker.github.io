
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