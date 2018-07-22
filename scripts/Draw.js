TweenLite.defaultEase = Linear.easeNone;

//show the square only once js has run
//visibility set to hidden in css panel
TweenLite.set(".square", {visibility:"visible"});



var tl = new TimelineLite(), tl2= new TimelineLite(), tl3 = new TimelineLite(), tl4 = new TimelineLite();

tl.fromTo(".l2", 4, {width:0}, {width:$('.table').outerWidth()});
tl2.fromTo(".l1", 4, {height:0}, {height:$(".table").outerHeight()});
tl3.fromTo(".l3", 4, {height:0}, {height:$(".table").outerHeight()});
tl4.fromTo(".l4", 4, {width:0}, {width:$('.table').outerWidth()});

tl.timeScale(4); //play faster
tl2.timeScale(4); //play faster
tl3.timeScale(4); //play faster
tl4.timeScale(4); //play faster

$('.square').css('height', $('.table').outerHeight());
<<<<<<< HEAD
$('page').css('min-height', $('.square').outerHeight()+100);
=======
>>>>>>> 74cf756e42dae67845461c00169dcd2f48b12629

$( window ).resize(function() {$(".l1").css("height", $(".table").outerHeight());});
$( window ).resize(function() {$('.l2').css('width', $('.table').outerWidth());});
$( window ).resize(function() {$('.l3').css('height', $('.table').outerHeight());});
$( window ).resize(function() {$('.l4').css('width', $('.table').outerWidth());});
$( window ).resize(function() {$('.square').css('height', $('.table').outerHeight());}); 
<<<<<<< HEAD
$( window ).resize(function() {$('page').css('min-height', $('.square').outerHeight()+100);}); 

jQuery(document).ready(function($){
    setTimeout(function(){
        $('.trans--growLeft').addClass('grow');
				$('.trans--growRight').addClass('grow');
    }, 275);
});
=======
$( window ).resize(function() {$('page').css('min-height', $('.table').outerHeight()+100);}); 

$('.trans--grow').addClass('grow');
>>>>>>> 74cf756e42dae67845461c00169dcd2f48b12629

