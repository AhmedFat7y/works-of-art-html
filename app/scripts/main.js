/* global Maplace chaptersTree */
'use strict';
$(document).ready(function(){
  // $.get('images/svg-defs.svg', function(data) {
  //   var $icons = $('<div class="icons"></div>').html(new XMLSerializer().serializeToString(data.documentElement));
  //   $('body').prepend($icons);
  // });

  if ($('#editor').length > 0) {
    var editor = new Quill('#editor', {
      modules: {
        'toolbar': { container: '#toolbar' },
        'link-tooltip': true
      },
      theme: 'snow',
    });
  }//endif
  
  $('.slider-1, .slider-2, .slider-3').slick({
    slidesToShow: 1,
    // slidesToScroll: 1,
    centerPadding: '10px',
    centerMode: true,
    adaptiveHeight: true,
    // asNavFor: '.slider-3',
    // focusOnSelect: true
  });
  
  $(chaptersTree).each(function(index, treeLevel) {
    var slider = $('.slider-' + (index+1));
    $(treeLevel).each(function(index2, chapter){
      slider.slick('slickAdd', chapter.html);
    });
  });
  
  $('.slider-1, .slider-2, .slider-3').slick('slickGoTo', 0);

  $('.slider-2').on('beforeChange', function(event, slick, currentSlide, nextSlide) {
    var id = slick.$slides[nextSlide].id;
    $('.slider-3').slick('slickFilter', '[data-parent=' + id + ']');
  });
  // $('').slick({
  //   slidesToShow: 3,
  //   slidesToScroll: 1,
  //   // asNavFor: '.slider-3',
  //   centerPadding: '10px',
  //   centerMode: true,
  //   focusOnSelect: true
  // });

  // $('').slick({
  //   slidesToShow: 3,
  //   slidesToScroll: 1,
  //   // asNavFor: '.slider-2',
  //   centerPadding: '10px',
  //   centerMode: true,
  //   focusOnSelect: true
  // });

});
