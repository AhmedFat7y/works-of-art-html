/* global Maplace */
'use strict';
$(document).ready(function(){
  $.get('images/svg-defs.svg', function(data) {
    var $icons = $('<div class="icons"></div>').html(new XMLSerializer().serializeToString(data.documentElement));
    $('body').prepend($icons);
  });
});
