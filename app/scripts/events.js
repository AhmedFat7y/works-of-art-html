/* global Maplace */
'use strict';
// $('.js-filter').on('click', function(){
//   if (filtered === false) {
//     $('.filtering').slick('slickFilter',':even');
//     $(this).text('Unfilter Slides');
//     filtered = true;
//   } else {
//     $('.filtering').slick('slickUnfilter');
//     $(this).text('Filter Slides');
//     filtered = false;
//   }
// });

$('.slider-1').on('click', '.slick-active.slick-center', function() {
  var slider1 = $('.slider-1');
  var slider2 = $('.slider-2');
  var slider3 = $('.slider-3');
  
  var slider1ChapterNumber = parseInt(slider1.prop('data-chapter'));
  var slider2ChapterNumber = parseInt(slider2.prop('data-chapter'));
  var slider3ChapterNumber = parseInt(slider3.prop('data-chapter'));
  if (slider1ChapterNumber <= 1) {
    return;
  }//endif
  replaceSlides(slider1, chaptersTree[slider1ChapterNumber - 2]);
  replaceSlides(slider2, chaptersTree[slider2ChapterNumber - 2]);
  replaceSlides(slider3, chaptersTree[slider3ChapterNumber - 2]);
  slider1.prop('data-chapter', slider1ChapterNumber - 1)
  slider2.prop('data-chapter', slider2ChapterNumber - 1)
  slider3.prop('data-chapter', slider3ChapterNumber - 1)
});

$('.slider-2 .slick-center').on('click', function() {

});

$('.slider-3').on('click', '.slick-active.slick-center', function() {
  var slider1 = $('.slider-1');
  var slider2 = $('.slider-2');
  var slider3 = $('.slider-3');
  
  var slider1ChapterNumber = parseInt(slider1.prop('data-chapter'));
  var slider2ChapterNumber = parseInt(slider2.prop('data-chapter'));
  var slider3ChapterNumber = parseInt(slider3.prop('data-chapter'));
  if ( maxChapterNumber <= slider3ChapterNumber) {
    return;
  }//endif
  replaceSlides(slider1, chaptersTree[slider1ChapterNumber]);
  replaceSlides(slider2, chaptersTree[slider2ChapterNumber]);
  replaceSlides(slider3, chaptersTree[slider3ChapterNumber]);
  slider1.prop('data-chapter', slider1ChapterNumber + 1)
  slider2.prop('data-chapter', slider2ChapterNumber + 1)
  slider3.prop('data-chapter', slider3ChapterNumber + 1)
});

$('.slider-1').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  var id = slick.$slides[nextSlide].id;
  $('.slider-2').slick('slickFilter', '[data-parent=' + id + ']');
});

$('.slider-2').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  var id = slick.$slides[nextSlide].id;
  $('.slider-3').slick('slickFilter', '[data-parent=' + id + ']');
});

$('.slider-3').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
  // var id = slick.$slides[nextSlide].id;
  // $('.slider-3').slick('slickFilter', '[data-parent=' + id + ']');
});