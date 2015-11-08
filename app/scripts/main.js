/* global Maplace */
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
  }
  
  $('.slider-for').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    arrows: true,
    fade: true,
    asNavFor: '.slider-nav'
  });

  $('.slider-nav').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.slider-for',
    centerPadding: '10px',
    centerMode: true,
    focusOnSelect: true
  });

});
