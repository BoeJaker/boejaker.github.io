TweenLite.defaultEase = Linear.easeNone;

//show the square only once js has run
//visibility set to hidden in css panel
TweenLite.set(".square", {visibility:"visible"});
// jQuery(document).ready(function($){
//     setTimeout(function(){
// $(".page").each(function() {

// var tl = new TimelineLite(), tl2= new TimelineLite(), tl3 = new TimelineLite(), tl4 = new TimelineLite();
// tl.fromTo($(this).find(".l2"), 4, {width:0}, {width:$(this).find('.table').outerWidth()});
// tl2.fromTo($(this).find(".l1"), 4, {height:0}, {height:$(this).find(".table").outerHeight()});
// tl3.fromTo($(this).find(".l3"), 4, {height:0}, {height:$(this).find(".table").outerHeight()});
// tl4.fromTo($(this).find(".l4"), 4, {width:0}, {width:$(this).find('.table').outerWidth()});

// tl.timeScale(4); //play faster
// tl2.timeScale(4); //play faster
// tl3.timeScale(4); //play faster
// tl4.timeScale(4); //play faster

// $(this).find('.square').css('min-height', $(this).find('.table').outerHeight());
// $(this).css('min-height', parseInt($(this).find('.square').outerHeight())+parseInt($(this).find('.banner').outerHeight())+100);


//         $('.trans--growLeft').addClass('grow');
// 				$('.trans--growRight').addClass('grow');
// });
// }, 340);
// });
// $( window ).resize(function() {$(".l1").css("height", $(".table").outerHeight());});
// $( window ).resize(function() {$('.l2').css('width', $('.table').outerWidth());});
// $( window ).resize(function() {$('.l3').css('height', $('.table').outerHeight());});
// $( window ).resize(function() {$('.l4').css('width', $('.table').outerWidth());});
// $( window ).resize(function() {$('.square').css('height', $('.table').outerHeight());}); 
// $( window ).resize(function() {$('page').css('min-height', parseInt($('.square').outerHeight())+parseInt($('.banner').outerHeight())+100)}); 


var tl = new TimelineLite(), tl2= new TimelineLite(), tl3 = new TimelineLite(), tl4 = new TimelineLite();
jQuery(document).ready(function($){
    setTimeout(function(){
tl.fromTo(".l2", 4, {width:0}, {width:$('.table').outerWidth()});
tl2.fromTo(".l1", 4, {height:0}, {height:$(".table").outerHeight()});
tl3.fromTo(".l3", 4, {height:0}, {height:$(".table").outerHeight()});
tl4.fromTo(".l4", 4, {width:0}, {width:$('.table').outerWidth()});

tl.timeScale(4); //play faster
tl2.timeScale(4); //play faster
tl3.timeScale(4); //play faster
tl4.timeScale(4); //play faster

$('.square').css('height', $('.table').outerHeight());
$('page').css('min-height', parseInt($('.square').outerHeight())+parseInt($('.banner').outerHeight())+100);


        $('.trans--growLeft').addClass('grow');
				$('.trans--growRight').addClass('grow');
    }, 340);
});
$( window ).resize(function() {$(".l1").css("height", $(".table").outerHeight());});
$( window ).resize(function() {$('.l2').css('width', $('.table').outerWidth());});
$( window ).resize(function() {$('.l3').css('height', $('.table').outerHeight());});
$( window ).resize(function() {$('.l4').css('width', $('.table').outerWidth());});
$( window ).resize(function() {$('.square').css('height', $('.table').outerHeight());}); 
$( window ).resize(function() {$('page').css('min-height', parseInt($('.square').outerHeight())+parseInt($('.banner').outerHeight())+100)}); 

