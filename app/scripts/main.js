/* global Maplace chaptersTree quillEditor */
'use strict';
$(document).ready(function(){
  // $.get('images/svg-defs.svg', function(data) {
  //   var $icons = $('<div class="icons"></div>').html(new XMLSerializer().serializeToString(data.documentElement));
  //   $('body').prepend($icons);
  // });

  if ($('#editor').length > 0) {
    quillEditor = new Quill('#editor', {
      modules: {
        'toolbar': { container: '#toolbar' },
        'link-tooltip': true
      },
      theme: 'snow',
    });
  }//endif
  
  $('.slider').slick({
    slidesToShow: 3,
    // slidesToScroll: 1,
    centerPadding: '10px',
    centerMode: true,
    adaptiveHeight: true,
    draggable: false,
    // asNavFor: '.slider-3',
    // focusOnSelect: true
  });
  
  $(chaptersTree).each(function(index, treeLevel) {
    var slider = $('.slider-' + (index + 1));
    slider.prop('data-chapter', index + 1);
    $(treeLevel).each(function(index2, chapter){
      slider.slick('slickAdd', chapter.html);
    });
  });
  
  // $('.slider-1, .slider-2, .slider-3').slick('slickGoTo', 0);

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
