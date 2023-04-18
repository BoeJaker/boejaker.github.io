
$(window).scroll(function(){
	if ($("page").outerHeight() <= $(window).height() ) {
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
		// $('html, body').stop().animate({scrollTop: posToScroll}, 200);
	}, 250));
		};
});
// $('page').on('touchmove', function() {
//   if ($('page').outerHeight() <= $(window).height()) {
//     clearTimeout($.data(this, 'scrollTimer'));
//     $.data(this, 'scrollTimer', setTimeout(function() {
//       var individualDivHeight = $('page').height();
//       var _cur_top = $(window).scrollTop();
//       var totalHeight = $('content').height();
//       var posToScroll = Math.round(_cur_top / individualDivHeight) * individualDivHeight;
//       // Use native browser scrolling instead of jQuery's animate()
//       $('html, body').css('scroll-behavior', 'smooth');
//       window.scrollTo({ top: posToScroll, behavior: 'smooth' });
//       $('html, body').stop().animate({scrollTop: posToScroll}, 200);
//     }, 250));
//   }
// });
const containers = document.querySelectorAll('.scroll-container');

containers.forEach(container => {
  const content = container.querySelector('.table');
  const scrollbar = document.createElement('div');
  const thumb = document.createElement('div');
  
  scrollbar.classList.add('scrollbar');
  thumb.classList.add('thumb');

  container.appendChild(scrollbar);
  scrollbar.appendChild(thumb);

  const updateScrollbar = () => {
    // Calculate scrollbar height
    const scrollbarHeight = (container.offsetHeight / content.scrollHeight * container.offsetHeight);

    // Set scrollbar height
    thumb.style.height = `${scrollbarHeight}px`;

    // Handle scroll event
    content.addEventListener('scroll', () => {
      const scrollTop = content.scrollTop;
      const maxScrollTop = content.scrollHeight - container.offsetHeight;
      const scrollPercentage = scrollTop / maxScrollTop;
      const scrollOffset = scrollPercentage * (container.offsetHeight - scrollbarHeight);

      // Move thumb
      thumb.style.transform = `translateY(${scrollOffset}px)`;
    });
  };

  updateScrollbar();

  window.addEventListener('resize', updateScrollbar);
  window.addEventListener('orientationchange', updateScrollbar);
});

// const container = document.querySelector('.scroll-container');
// const content = document.querySelector('.table');
// const scrollbar = document.querySelector('.scrollbar');
// const thumb = document.querySelector('.thumb');

// // Calculate scrollbar height
// const scrollbarHeight = (container.offsetHeight / content.scrollHeight * container.offsetHeight);

// // Set scrollbar height
// thumb.style.height = `${scrollbarHeight}px`;

// // Handle scroll event
// content.addEventListener('scroll', () => {
//   const scrollTop = content.scrollTop;
//   const maxScrollTop = content.scrollHeight - container.offsetHeight;
//   const scrollPercentage = scrollTop / maxScrollTop;
//   const scrollOffset = scrollPercentage * (container.offsetHeight - scrollbarHeight);

//   // Move thumb
//   thumb.style.transform = `translateY(${scrollOffset}px)`;
// });

// var container = document.getElementById(".square");
//   var content = document.getElementById(".table");

//   function updateSize() {
//     var containerWidth = container.clientHeight;
//     var contentWidth = content.scrollHeight;

//     // if (contentWidth > containerWidth) {
//     //   container.style.overflowY = "scroll";
//     // //   container.style.paddingBottom = "17px"; // add space for scrollbar
//     // } else {
//     //   container.style.overflowY = "hidden";
//     // //   container.style.paddingBottom = "0";
//     // }
//   }

//   window.addEventListener("load", updateSize);
//   window.addEventListener("orientationchange", updateSize);